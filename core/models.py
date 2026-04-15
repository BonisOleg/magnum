from django.db import models
from django.utils.translation import gettext_lazy as _
import cloudinary.models


class CompanyInfo(models.Model):
    email = models.EmailField(_("Email"), default="magnum_tvk@ukr.net")
    phone = models.CharField(_("Телефон"), max_length=32, default="+38 073 3 777 333")
    address = models.CharField(_("Адреса"), max_length=255, default="49102, м. Дніпро, вул. Волинська, 46")
    city = models.CharField(_("Місто"), max_length=100, default="Дніпро")
    postal_code = models.CharField(_("Поштовий індекс"), max_length=20, default="49102")
    street_address = models.CharField(_("Вулиця"), max_length=255, default="вул. Волинська, 46")
    telegram = models.CharField(_("Telegram"), max_length=255, blank=True)
    viber = models.CharField(_("Viber"), max_length=32, blank=True)
    instagram = models.URLField(_("Instagram"), blank=True)
    facebook = models.URLField(_("Facebook"), blank=True)

    class Meta:
        verbose_name = _("Інформація про компанію")
        verbose_name_plural = _("Інформація про компанію")

    def __str__(self):
        return "Magnum — Інформація про компанію"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class ContactRequest(models.Model):
    name = models.CharField(_("Ім'я"), max_length=150)
    email = models.EmailField(_("Email"), blank=True)
    phone = models.CharField(_("Телефон"), max_length=32, blank=True)
    message = models.TextField(_("Повідомлення"))
    is_processed = models.BooleanField(_("Оброблено"), default=False)
    created_at = models.DateTimeField(_("Дата"), auto_now_add=True)

    class Meta:
        verbose_name = _("Заявка")
        verbose_name_plural = _("Заявки")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.created_at:%d.%m.%Y %H:%M}"


class SiteSettings(models.Model):
    site_name = models.CharField(_("Назва сайту"), max_length=100, default="Magnum")
    tagline = models.CharField(_("Слоган"), max_length=255, default="Виробництво якісного пакування")
    copyright_text = models.CharField(_("Текст авторських прав"), max_length=255, default="Всі права захищені")
    logo = cloudinary.models.CloudinaryField(_("Логотип"), blank=True, null=True)
    favicon = cloudinary.models.CloudinaryField(_("Favicon"), blank=True, null=True)
    og_image = cloudinary.models.CloudinaryField(_("OG зображення"), blank=True, null=True)
    default_meta_title = models.CharField(_("Дефолтний Meta Title"), max_length=255, blank=True)
    default_meta_description = models.TextField(_("Дефолтний Meta Description"), blank=True)

    class Meta:
        verbose_name = _("Налаштування сайту")
        verbose_name_plural = _("Налаштування сайту")

    def __str__(self):
        return "Налаштування сайту"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class HeroSection(models.Model):
    eyebrow = models.CharField(_("Підзаголовок"), max_length=255, blank=True)
    title = models.CharField(_("Заголовок"), max_length=255)
    subtitle = models.TextField(_("Підтекст"))
    background_image = cloudinary.models.CloudinaryField(_("Фоново зображення"), blank=True, null=True)
    cta_primary_text = models.CharField(_("Основна CTA текст"), max_length=100, blank=True)
    cta_primary_url = models.CharField(_("Основна CTA посилання"), max_length=500, blank=True)
    cta_secondary_text = models.CharField(_("Вторинна CTA текст"), max_length=100, blank=True)
    cta_secondary_url = models.CharField(_("Вторинна CTA посилання"), max_length=500, blank=True)

    class Meta:
        verbose_name = _("Hero секція")
        verbose_name_plural = _("Hero секція")

    def __str__(self):
        return "Hero секція"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class ServiceItem(models.Model):
    title = models.CharField(_("Назва"), max_length=255)
    description = models.TextField(_("Опис"))
    icon_svg = models.TextField(_("SVG іконка"), blank=True)
    order = models.PositiveIntegerField(_("Порядок"), default=0)
    is_active = models.BooleanField(_("Активний"), default=True)

    class Meta:
        verbose_name = _("Сервіс")
        verbose_name_plural = _("Сервіси")
        ordering = ["order"]

    def __str__(self):
        return self.title


class BagType(models.Model):
    title = models.CharField(_("Назва"), max_length=255)
    description = models.TextField(_("Опис"))
    icon_svg = models.TextField(_("SVG іконка"), blank=True)
    feature_1 = models.CharField(_("Особливість 1"), max_length=255, blank=True)
    feature_2 = models.CharField(_("Особливість 2"), max_length=255, blank=True)
    feature_3 = models.CharField(_("Особливість 3"), max_length=255, blank=True)
    order = models.PositiveIntegerField(_("Порядок"), default=0)
    is_active = models.BooleanField(_("Активний"), default=True)

    class Meta:
        verbose_name = _("Тип пакету")
        verbose_name_plural = _("Типи пакетів")
        ordering = ["order"]

    def __str__(self):
        return self.title


class FlexoSection(models.Model):
    title = models.CharField(_("Заголовок"), max_length=255)
    lead_text = models.TextField(_("Вступний текст"))
    body_text = models.TextField(_("Основний текст"))
    cta_text = models.CharField(_("CTA текст"), max_length=100, blank=True)
    cta_url = models.CharField(_("CTA посилання"), max_length=500, blank=True)

    class Meta:
        verbose_name = _("Флексодрук секція")
        verbose_name_plural = _("Флексодрук секція")

    def __str__(self):
        return "Флексодрук секція"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class FlexoBenefit(models.Model):
    flexo = models.ForeignKey(FlexoSection, on_delete=models.CASCADE, related_name="benefits", verbose_name=_("Флексодрук"))
    title = models.CharField(_("Назва"), max_length=255)
    text = models.TextField(_("Опис"))
    icon_svg = models.TextField(_("SVG іконка"), blank=True)
    order = models.PositiveIntegerField(_("Порядок"), default=0)

    class Meta:
        verbose_name = _("Перевага флексодруку")
        verbose_name_plural = _("Переваги флексодруку")
        ordering = ["order"]

    def __str__(self):
        return self.title


class AboutSection(models.Model):
    title = models.CharField(_("Заголовок"), max_length=255)
    lead_text = models.TextField(_("Вступний текст"))
    body_text = models.TextField(_("Основний текст"))

    class Meta:
        verbose_name = _("Про компанію секція")
        verbose_name_plural = _("Про компанію секція")

    def __str__(self):
        return "Про компанію"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class AboutFeature(models.Model):
    about = models.ForeignKey(AboutSection, on_delete=models.CASCADE, related_name="features", verbose_name=_("Про компанію"))
    text = models.CharField(_("Текст"), max_length=255)
    order = models.PositiveIntegerField(_("Порядок"), default=0)

    class Meta:
        verbose_name = _("Особливість")
        verbose_name_plural = _("Особливості")
        ordering = ["order"]

    def __str__(self):
        return self.text


class AboutStat(models.Model):
    about = models.ForeignKey(AboutSection, on_delete=models.CASCADE, related_name="stats", verbose_name=_("Про компанію"))
    value = models.CharField(_("Значення"), max_length=100)
    label = models.CharField(_("Назва"), max_length=255)
    order = models.PositiveIntegerField(_("Порядок"), default=0)

    class Meta:
        verbose_name = _("Статистика")
        verbose_name_plural = _("Статистика")
        ordering = ["order"]

    def __str__(self):
        return f"{self.value} — {self.label}"


class Testimonial(models.Model):
    name = models.CharField(_("Ім'я"), max_length=255)
    text = models.TextField(_("Відгук"))
    role = models.CharField(_("Роль"), max_length=255, blank=True)
    avatar = cloudinary.models.CloudinaryField(_("Аватар"), blank=True, null=True)
    order = models.PositiveIntegerField(_("Порядок"), default=0)
    is_active = models.BooleanField(_("Активний"), default=True)

    class Meta:
        verbose_name = _("Відгук")
        verbose_name_plural = _("Відгуки")
        ordering = ["order"]

    def __str__(self):
        return f"{self.name} — {self.role}"


class ContactSection(models.Model):
    title = models.CharField(_("Заголовок"), max_length=255)
    intro_text = models.TextField(_("Вступний текст"))

    class Meta:
        verbose_name = _("Контакти секція")
        verbose_name_plural = _("Контакти секція")

    def __str__(self):
        return "Контакти"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class CatalogPageContent(models.Model):
    title = models.CharField(_("Заголовок"), max_length=255)
    description = models.TextField(_("Опис"))
    hero_title = models.CharField(_("Hero заголовок"), max_length=255, blank=True)
    hero_description = models.TextField(_("Hero опис"), blank=True)
    order_cta_text = models.CharField(_("Кнопка замовлення (товар)"), max_length=150, blank=True)
    product_desc_heading = models.CharField(_("Заголовок опису товару"), max_length=150, blank=True)
    related_heading = models.CharField(_("Заголовок схожих товарів"), max_length=150, blank=True)
    cta_title = models.CharField(_("CTA заголовок"), max_length=255, blank=True)
    cta_description = models.TextField(_("CTA опис"), blank=True)
    cta_button_text = models.CharField(_("CTA текст кнопки"), max_length=100, blank=True)

    class Meta:
        verbose_name = _("Контент каталогу")
        verbose_name_plural = _("Контент каталогу")

    def __str__(self):
        return "Контент каталогу"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class ServicesSection(models.Model):
    title = models.CharField(_("Заголовок секції"), max_length=255)
    subtitle = models.CharField(_("Підзаголовок секції"), max_length=500, blank=True)

    class Meta:
        verbose_name = _("Секція — Сервіси")
        verbose_name_plural = _("Секція — Сервіси")

    def __str__(self):
        return "Секція сервісів"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class BagsSection(models.Model):
    title = models.CharField(_("Заголовок секції"), max_length=255)
    subtitle = models.CharField(_("Підзаголовок секції"), max_length=500, blank=True)

    class Meta:
        verbose_name = _("Секція — Типи пакетів")
        verbose_name_plural = _("Секція — Типи пакетів")

    def __str__(self):
        return "Секція типів пакетів"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class CatalogPreviewSection(models.Model):
    title = models.CharField(_("Заголовок секції"), max_length=255)
    subtitle = models.CharField(_("Підзаголовок секції"), max_length=500, blank=True)
    cta_button_text = models.CharField(_("Текст кнопки CTA"), max_length=100, blank=True)

    class Meta:
        verbose_name = _("Секція — Популярна продукція")
        verbose_name_plural = _("Секція — Популярна продукція")

    def __str__(self):
        return "Секція популярної продукції"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class CurrencySection(models.Model):
    title = models.CharField(_("Заголовок секції"), max_length=255)
    subtitle = models.CharField(_("Підзаголовок секції"), max_length=500, blank=True)

    class Meta:
        verbose_name = _("Секція — Курс валют")
        verbose_name_plural = _("Секція — Курс валют")

    def __str__(self):
        return "Секція курсу валют"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class TestimonialsSection(models.Model):
    title = models.CharField(_("Заголовок секції"), max_length=255)

    class Meta:
        verbose_name = _("Секція — Відгуки")
        verbose_name_plural = _("Секція — Відгуки")

    def __str__(self):
        return "Секція відгуків"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj
