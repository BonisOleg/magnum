from modeltranslation.translator import register, TranslationOptions
from .models import (
    CompanyInfo, SiteSettings, HeroSection, ServiceItem, BagType,
    FlexoSection, FlexoBenefit, AboutSection, AboutFeature, AboutStat,
    Testimonial, ContactSection, CatalogPageContent,
    ServicesSection, BagsSection, CatalogPreviewSection,
    CurrencySection, TestimonialsSection,
)


@register(CompanyInfo)
class CompanyInfoTranslationOptions(TranslationOptions):
    fields = ("address", "city", "street_address")


@register(SiteSettings)
class SiteSettingsTranslationOptions(TranslationOptions):
    fields = ("site_name", "tagline", "copyright_text", "default_meta_title", "default_meta_description")


@register(HeroSection)
class HeroSectionTranslationOptions(TranslationOptions):
    fields = ("eyebrow", "title", "subtitle", "cta_primary_text", "cta_primary_url", "cta_secondary_text", "cta_secondary_url")


@register(ServiceItem)
class ServiceItemTranslationOptions(TranslationOptions):
    fields = ("title", "description")


@register(BagType)
class BagTypeTranslationOptions(TranslationOptions):
    fields = ("title", "description", "feature_1", "feature_2", "feature_3")


@register(FlexoSection)
class FlexoSectionTranslationOptions(TranslationOptions):
    fields = ("title", "lead_text", "body_text", "cta_text", "cta_url")


@register(FlexoBenefit)
class FlexoBenefitTranslationOptions(TranslationOptions):
    fields = ("title", "text")


@register(AboutSection)
class AboutSectionTranslationOptions(TranslationOptions):
    fields = ("title", "lead_text", "body_text")


@register(AboutFeature)
class AboutFeatureTranslationOptions(TranslationOptions):
    fields = ("text",)


@register(AboutStat)
class AboutStatTranslationOptions(TranslationOptions):
    fields = ("value", "label")


@register(Testimonial)
class TestimonialTranslationOptions(TranslationOptions):
    fields = ("name", "text", "role")


@register(ContactSection)
class ContactSectionTranslationOptions(TranslationOptions):
    fields = ("title", "intro_text")


@register(CatalogPageContent)
class CatalogPageContentTranslationOptions(TranslationOptions):
    fields = (
        "title", "description",
        "hero_title", "hero_description",
        "order_cta_text", "product_desc_heading", "related_heading",
        "cta_title", "cta_description", "cta_button_text",
    )


@register(ServicesSection)
class ServicesSectionTranslationOptions(TranslationOptions):
    fields = ("title", "subtitle")


@register(BagsSection)
class BagsSectionTranslationOptions(TranslationOptions):
    fields = ("title", "subtitle")


@register(CatalogPreviewSection)
class CatalogPreviewSectionTranslationOptions(TranslationOptions):
    fields = ("title", "subtitle", "cta_button_text")


@register(CurrencySection)
class CurrencySectionTranslationOptions(TranslationOptions):
    fields = ("title", "subtitle")


@register(TestimonialsSection)
class TestimonialsSectionTranslationOptions(TranslationOptions):
    fields = ("title",)
