from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from .models import (
    CompanyInfo, ContactRequest, SiteSettings, HeroSection, ServiceItem, BagType,
    FlexoSection, FlexoBenefit, AboutSection, AboutFeature, AboutStat,
    Testimonial, ContactSection, CatalogPageContent,
    ServicesSection, BagsSection, CatalogPreviewSection,
    CurrencySection, TestimonialsSection,
)


@admin.register(CompanyInfo)
class CompanyInfoAdmin(TranslationAdmin):
    fieldsets = (
        (_("Контакти"), {"fields": ("email", "phone")}),
        (_("Адреса"), {"fields": ("address", "city", "postal_code", "street_address")}),
        (_("Соцмережі"), {"fields": ("telegram", "viber", "instagram", "facebook")}),
    )

    def has_add_permission(self, request):
        return not CompanyInfo.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email", "is_processed", "created_at")
    list_filter = ("is_processed", "created_at")
    search_fields = ("name", "email", "phone", "message")
    list_editable = ("is_processed",)
    readonly_fields = ("name", "email", "phone", "message", "created_at")
    ordering = ("-created_at",)


@admin.register(SiteSettings)
class SiteSettingsAdmin(TranslationAdmin):
    fieldsets = (
        (_("Брендинг"), {"fields": ("site_name", "tagline", "copyright_text")}),
        (_("Медіа"), {"fields": ("logo", "favicon", "og_image")}),
        (_("SEO"), {"fields": ("default_meta_title", "default_meta_description")}),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(HeroSection)
class HeroSectionAdmin(TranslationAdmin):
    fieldsets = (
        (_("Основне"), {"fields": ("eyebrow", "title", "subtitle")}),
        (_("Зображення"), {"fields": ("background_image",)}),
        (_("CTA"), {"fields": (("cta_primary_text", "cta_primary_url"), ("cta_secondary_text", "cta_secondary_url"))}),
    )

    def has_add_permission(self, request):
        return not HeroSection.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(ServiceItem)
class ServiceItemAdmin(TranslationAdmin):
    list_display = ("title", "order", "is_active")
    list_editable = ("order", "is_active")
    fieldsets = (
        (_("Основне"), {"fields": ("title", "description", "icon_svg")}),
        (_("Видимість"), {"fields": ("order", "is_active")}),
    )


@admin.register(BagType)
class BagTypeAdmin(TranslationAdmin):
    list_display = ("title", "order", "is_active")
    list_editable = ("order", "is_active")
    fieldsets = (
        (_("Основне"), {"fields": ("title", "description", "icon_svg")}),
        (_("Особливості"), {"fields": ("feature_1", "feature_2", "feature_3")}),
        (_("Видимість"), {"fields": ("order", "is_active")}),
    )


class FlexoBenefitInline(TranslationTabularInline):
    model = FlexoBenefit
    extra = 1
    fields = ("title", "text", "icon_svg", "order")


@admin.register(FlexoSection)
class FlexoSectionAdmin(TranslationAdmin):
    inlines = [FlexoBenefitInline]
    fieldsets = (
        (_("Основне"), {"fields": ("title", "lead_text", "body_text")}),
        (_("CTA"), {"fields": (("cta_text", "cta_url"),)}),
    )

    def has_add_permission(self, request):
        return not FlexoSection.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


class AboutFeatureInline(TranslationTabularInline):
    model = AboutFeature
    extra = 1
    fields = ("text", "order")


class AboutStatInline(TranslationTabularInline):
    model = AboutStat
    extra = 1
    fields = ("value", "label", "order")


@admin.register(AboutSection)
class AboutSectionAdmin(TranslationAdmin):
    inlines = [AboutFeatureInline, AboutStatInline]
    fieldsets = (
        (_("Основне"), {"fields": ("title", "lead_text", "body_text")}),
    )

    def has_add_permission(self, request):
        return not AboutSection.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Testimonial)
class TestimonialAdmin(TranslationAdmin):
    list_display = ("name", "role", "order", "is_active")
    list_editable = ("order", "is_active")
    fieldsets = (
        (_("Основне"), {"fields": ("name", "role", "text", "avatar")}),
        (_("Видимість"), {"fields": ("order", "is_active")}),
    )


@admin.register(ContactSection)
class ContactSectionAdmin(TranslationAdmin):
    fieldsets = (
        (_("Основне"), {"fields": ("title", "intro_text")}),
    )

    def has_add_permission(self, request):
        return not ContactSection.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(CatalogPageContent)
class CatalogPageContentAdmin(TranslationAdmin):
    fieldsets = (
        (_("Службовий заголовок"), {"fields": ("title", "description")}),
        (_("Hero каталогу"), {"fields": ("hero_title", "hero_description")}),
        (_("Сторінка товару"), {"fields": ("order_cta_text", "product_desc_heading", "related_heading")}),
        (_("CTA блок"), {"fields": ("cta_title", "cta_description", "cta_button_text")}),
    )

    def has_add_permission(self, request):
        return not CatalogPageContent.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(ServicesSection)
class ServicesSectionAdmin(TranslationAdmin):
    fieldsets = (
        (_("Заголовок секції сервісів"), {"fields": ("title", "subtitle")}),
    )

    def has_add_permission(self, request):
        return not ServicesSection.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(BagsSection)
class BagsSectionAdmin(TranslationAdmin):
    fieldsets = (
        (_("Заголовок секції типів пакетів"), {"fields": ("title", "subtitle")}),
    )

    def has_add_permission(self, request):
        return not BagsSection.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(CatalogPreviewSection)
class CatalogPreviewSectionAdmin(TranslationAdmin):
    fieldsets = (
        (_("Секція популярної продукції"), {"fields": ("title", "subtitle", "cta_button_text")}),
    )

    def has_add_permission(self, request):
        return not CatalogPreviewSection.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(CurrencySection)
class CurrencySectionAdmin(TranslationAdmin):
    fieldsets = (
        (_("Секція курсу валют"), {"fields": ("title", "subtitle")}),
    )

    def has_add_permission(self, request):
        return not CurrencySection.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(TestimonialsSection)
class TestimonialsSectionAdmin(TranslationAdmin):
    fieldsets = (
        (_("Секція відгуків"), {"fields": ("title",)}),
    )

    def has_add_permission(self, request):
        return not TestimonialsSection.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
