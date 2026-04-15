import json
import logging
import urllib.request

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

from catalog.models import Product, ProductCategory
from .forms import ContactForm
from .models import (
    HeroSection, ServiceItem, BagType, FlexoSection, AboutSection,
    Testimonial, ContactSection,
    ServicesSection, BagsSection, CatalogPreviewSection,
    CurrencySection, TestimonialsSection,
)

logger = logging.getLogger(__name__)

_NBU_API_URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
_CURRENCY_CODES = {"USD", "EUR"}


def _get_exchange_rates() -> dict:
    """Fetch USD and EUR rates from the National Bank of Ukraine API."""
    try:
        with urllib.request.urlopen(_NBU_API_URL, timeout=4) as resp:
            data = json.loads(resp.read().decode())
        rates = {}
        for item in data:
            if item.get("cc") in _CURRENCY_CODES:
                rates[item["cc"]] = {
                    "rate": round(item["rate"], 2),
                    "date": item.get("exchangedate", ""),
                }
        return rates
    except Exception:
        logger.warning("Failed to fetch NBU exchange rates")
        return {}


def landing(request):
    categories = ProductCategory.objects.filter(is_active=True).order_by("order")
    featured = Product.objects.filter(is_active=True).exclude(slug="").order_by("order")[:6]

    hero = HeroSection.get()
    services = ServiceItem.objects.filter(is_active=True).order_by("order")
    bag_types = BagType.objects.filter(is_active=True).order_by("order")
    flexo = FlexoSection.get()
    flexo_benefits = flexo.benefits.all().order_by("order")
    about = AboutSection.get()
    about_features = about.features.all().order_by("order")
    about_stats = about.stats.all().order_by("order")
    testimonials = Testimonial.objects.filter(is_active=True).order_by("order")
    contact_section = ContactSection.get()

    services_section = ServicesSection.get()
    bags_section = BagsSection.get()
    catalog_preview = CatalogPreviewSection.get()
    currency_section = CurrencySection.get()
    testimonials_section = TestimonialsSection.get()

    exchange_rates = _get_exchange_rates()
    form = ContactForm()

    return render(request, "core/landing.html", {
        "hero": hero,
        "services": services,
        "services_section": services_section,
        "bag_types": bag_types,
        "bags_section": bags_section,
        "flexo": flexo,
        "flexo_benefits": flexo_benefits,
        "about": about,
        "about_features": about_features,
        "about_stats": about_stats,
        "categories": categories,
        "featured": featured,
        "catalog_preview": catalog_preview,
        "testimonials": testimonials,
        "testimonials_section": testimonials_section,
        "contact_section": contact_section,
        "currency_section": currency_section,
        "exchange_rates": exchange_rates,
        "form": form,
        "page_title": _("Magnum — Виробництво пакування"),
        "meta_description": _(
            "Magnum — виробництво якісних пакетів та плівки у Дніпрі. "
            "Флексодрук, індивідуальний дизайн, доставка по Україні."
        ),
    })


def _send_contact_notification(contact) -> None:
    """Send an email notification to the manager when a new contact request arrives."""
    recipient = settings.CONTACT_EMAIL
    if not recipient or not settings.EMAIL_HOST_USER:
        return
    subject = f"Нова заявка від {contact.name}"
    body = (
        f"Ім'я: {contact.name}\n"
        f"Телефон: {contact.phone}\n"
        f"Email: {contact.email or '—'}\n\n"
        f"Повідомлення:\n{contact.message}"
    )
    try:
        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [recipient], fail_silently=False)
    except Exception:
        logger.exception("Failed to send contact notification email for request id=%s", contact.pk)


def contact_submit(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            _send_contact_notification(contact)
            return render(request, "partials/contact_success.html")
        return render(request, "partials/contact_form.html", {"form": form})
    return HttpResponse(status=405)
