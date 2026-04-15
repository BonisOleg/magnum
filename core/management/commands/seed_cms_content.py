from django.core.management.base import BaseCommand
from django.utils.translation import gettext_lazy as _
from core.models import (
    SiteSettings, HeroSection, ServiceItem, BagType, FlexoSection, FlexoBenefit,
    AboutSection, AboutFeature, AboutStat, Testimonial, ContactSection, CatalogPageContent,
    ServicesSection, BagsSection, CatalogPreviewSection, CurrencySection, TestimonialsSection,
    CompanyInfo,
)


class Command(BaseCommand):
    help = "Seed CMS content from hardcoded data"

    def handle(self, *args, **options):
        self.stdout.write("Starting CMS content seeding...")

        self._seed_site_settings()
        self._seed_hero_section()
        self._seed_services()
        self._seed_services_section()
        self._seed_bag_types()
        self._seed_bags_section()
        self._seed_flexo_section()
        self._seed_about_section()
        self._seed_testimonials()
        self._seed_testimonials_section()
        self._seed_contact_section()
        self._seed_catalog_content()
        self._seed_catalog_preview_section()
        self._seed_currency_section()
        self._seed_company_info_extra()

        self.stdout.write(self.style.SUCCESS("CMS content seeding completed!"))

    def _seed_site_settings(self):
        settings, _ = SiteSettings.objects.get_or_create(pk=1)
        settings.site_name_uk = "Magnum"
        settings.site_name_en = "Magnum"
        settings.tagline_uk = "Виробництво якісного пакування"
        settings.tagline_en = "Manufacturing quality packaging"
        settings.copyright_text_uk = "Всі права захищені"
        settings.copyright_text_en = "All rights reserved"
        settings.default_meta_title_uk = "Magnum — Виробництво упаковки"
        settings.default_meta_title_en = "Magnum — Manufacturing packaging"
        settings.default_meta_description_uk = "Magnum — виробництво якісних пакетів та плівки у Дніпрі. Флексодрук, індивідуальний дизайн, доставка по Україні."
        settings.default_meta_description_en = "Magnum — manufacturing quality packaging in Dnipro. Flexoprinting, custom design, delivery across Ukraine."
        settings.save()
        self.stdout.write(self.style.SUCCESS("✓ SiteSettings seeded"))

    def _seed_hero_section(self):
        hero, _ = HeroSection.objects.get_or_create(pk=1)
        hero.eyebrow_uk = "Власне виробництво · Дніпро"
        hero.eyebrow_en = "Own production · Dnipro"
        hero.title_uk = "Упаковка,\nщо захищає\nваш бренд"
        hero.title_en = "Packaging that\nprotects your\nbrand"
        hero.subtitle_uk = "Пакети та плівки від виробника. Флексодрук, індивідуальний дизайн, доставка по Україні."
        hero.subtitle_en = "Packaging and film from the manufacturer. Flexoprinting, custom design, delivery across Ukraine."
        hero.cta_primary_text_uk = "Переглянути каталог"
        hero.cta_primary_text_en = "View catalog"
        hero.cta_primary_url = "/catalog/"
        hero.cta_secondary_text_uk = "Зв'язатися з нами"
        hero.cta_secondary_text_en = "Contact us"
        hero.cta_secondary_url = "#contact"
        hero.save()
        self.stdout.write(self.style.SUCCESS("✓ HeroSection seeded"))

    def _seed_services(self):
        services_data = [
            {
                "title_uk": "Виробництво пакування",
                "title_en": "Packaging Manufacturing",
                "description_uk": "Пакети різних розмірів і щільності: Wicket, BOPP, LDPE, HDPE, біорозкладні, дой-пак. Власне виробництво без залежності від посередників.",
                "description_en": "Bags of various sizes and densities: Wicket, BOPP, LDPE, HDPE, biodegradable, doy-pack. Own production without middlemen.",
                "order": 1,
            },
            {
                "title_uk": "Флексодрук на плівці",
                "title_en": "Flexoprinting on film",
                "description_uk": "Нанесення зображень на плівку та гнучкі матеріали. До 8 кольорів — повнота відтінків, чіткі межі, оптимальний контраст.",
                "description_en": "Applying images to film and flexible materials. Up to 8 colors — full tones, sharp edges, optimal contrast.",
                "order": 2,
            },
            {
                "title_uk": "Розробка дизайну",
                "title_en": "Design Development",
                "description_uk": "Розробка дизайну упаковки та переддрукарська підготовка макетів. Перетворюємо ідею на готовий файл для друку.",
                "description_en": "Packaging design and pre-print preparation of layouts. We turn ideas into ready-to-print files.",
                "order": 3,
            },
            {
                "title_uk": "Організація перевезень",
                "title_en": "Transportation Organization",
                "description_uk": "Логістика та доставка продукції по всій Україні. Оперативне виконання замовлень будь-якого обсягу.",
                "description_en": "Logistics and delivery of products throughout Ukraine. Quick fulfillment of orders of any volume.",
                "order": 4,
            },
        ]

        for data in services_data:
            service, _ = ServiceItem.objects.get_or_create(
                order=data["order"],
                defaults={"title_uk": data["title_uk"], "title_en": data["title_en"]}
            )
            service.title_uk = data["title_uk"]
            service.title_en = data["title_en"]
            service.description_uk = data["description_uk"]
            service.description_en = data["description_en"]
            service.is_active = True
            service.save()

        self.stdout.write(self.style.SUCCESS("✓ ServiceItem seeded"))

    def _seed_bag_types(self):
        bags_data = [
            {
                "title_uk": "Прямі пакети",
                "title_en": "Straight bags",
                "description_uk": "Класичний плоский пакет без складок. Підходить для пакування текстилю, документів, дрібного товару.",
                "description_en": "Classic flat bag without folds. Suitable for packaging textiles, documents, small items.",
                "feature_1_uk": "LDPE / HDPE / BOPP",
                "feature_1_en": "LDPE / HDPE / BOPP",
                "feature_2_uk": "Прозорі або кольорові",
                "feature_2_en": "Clear or colored",
                "feature_3_uk": "Можливий флексодрук",
                "feature_3_en": "Flexoprinting available",
                "order": 1,
            },
            {
                "title_uk": "Пакети з дном",
                "title_en": "Bags with bottom",
                "description_uk": "Об'ємна бокова або донна складка — пакет стійко тримається на полиці та вміщує більше.",
                "description_en": "Voluminous side or bottom fold — the bag stands stably on the shelf and holds more.",
                "feature_1_uk": "Бокова або донна складка",
                "feature_1_en": "Side or bottom fold",
                "feature_2_uk": "Стійкий на полиці",
                "feature_2_en": "Stable on shelf",
                "feature_3_uk": "Для сипких та штучних товарів",
                "feature_3_en": "For bulk and individual goods",
                "order": 2,
            },
            {
                "title_uk": "З липкою стрічкою",
                "title_en": "With adhesive tape",
                "description_uk": "Клапан із самоклейною стрічкою дозволяє повторно закривати пакет. Ідеально для косметики, текстилю, запчастин.",
                "description_en": "A flap with self-adhesive tape allows you to close the bag again. Ideal for cosmetics, textiles, spare parts.",
                "feature_1_uk": "Повторне закриття",
                "feature_1_en": "Reclosable",
                "feature_2_uk": "Захист від пилу",
                "feature_2_en": "Dust protection",
                "feature_3_uk": "Різні формати клапану",
                "feature_3_en": "Various flap formats",
                "order": 3,
            },
            {
                "title_uk": "З перфорацією",
                "title_en": "With perforation",
                "description_uk": "«Дихаюча» упаковка з мікро або макро отворами. Нормалізує вологість, продовжує свіжість продукту.",
                "description_en": "Breathable packaging with micro or macro holes. Normalizes moisture, extends product freshness.",
                "feature_1_uk": "Мікро та макро перфорація",
                "feature_1_en": "Micro and macro perforation",
                "feature_2_uk": "Для зелені, хліба, квітів",
                "feature_2_en": "For greens, bread, flowers",
                "feature_3_uk": "Без накопичення конденсату",
                "feature_3_en": "No condensation buildup",
                "order": 4,
            },
            {
                "title_uk": "З єврослотом",
                "title_en": "With euro slot",
                "description_uk": "Отвір у шапці пакету для підвішування на гачку. Зручна викладка на стійках у роздрібній торгівлі.",
                "description_en": "Hole in the bag's header for hanging on a hook. Convenient display on shelves in retail.",
                "feature_1_uk": "Стандартний єврослот",
                "feature_1_en": "Standard euro slot",
                "feature_2_uk": "Підвіска на гачку-дисплеї",
                "feature_2_en": "Hanging on hook display",
                "feature_3_uk": "Ефектна викладка товару",
                "feature_3_en": "Effective product display",
                "order": 5,
            },
            {
                "title_uk": "Конусні пакети",
                "title_en": "Conical bags",
                "description_uk": "Конічна форма — класичне рішення для квітів, рослин і пресованих букетів.",
                "description_en": "Conical shape — classic solution for flowers, plants and pressed bouquets.",
                "feature_1_uk": "Прозорі та з друком",
                "feature_1_en": "Clear and printed",
                "feature_2_uk": "BOPP / CPP",
                "feature_2_en": "BOPP / CPP",
                "feature_3_uk": "Для квітів і зелені",
                "feature_3_en": "For flowers and greens",
                "order": 6,
            },
            {
                "title_uk": "Дой-пак (стоячий)",
                "title_en": "Doy-pack (standing)",
                "description_uk": "Зварне дно дозволяє пакету стояти самостійно. Застосовується для кави, горіхів, сипких продуктів.",
                "description_en": "Welded bottom allows the bag to stand on its own. Used for coffee, nuts, bulk products.",
                "feature_1_uk": "Стійка на полиці форма",
                "feature_1_en": "Shelf-stable shape",
                "feature_2_uk": "Опціональна застібка zip-lock",
                "feature_2_en": "Optional zip-lock closure",
                "feature_3_uk": "Барьєрні матеріали",
                "feature_3_en": "Barrier materials",
                "order": 7,
            },
            {
                "title_uk": "Вікет-пакети (Wicket)",
                "title_en": "Wicket bags",
                "description_uk": "Блок пакетів на металевому дроті для швидкої автоматичної упаковки хлібобулочних та кондитерських виробів.",
                "description_en": "Block of bags on wire for fast automatic packaging of bakery and confectionery products.",
                "feature_1_uk": "Автоматична подача",
                "feature_1_en": "Automatic feeding",
                "feature_2_uk": "Для пекарень і кондитерських",
                "feature_2_en": "For bakeries and confectioneries",
                "feature_3_uk": "LDPE / HDPE",
                "feature_3_en": "LDPE / HDPE",
                "order": 8,
            },
        ]

        for data in bags_data:
            bag, _ = BagType.objects.get_or_create(
                order=data["order"],
                defaults={"title_uk": data["title_uk"], "title_en": data["title_en"]}
            )
            bag.title_uk = data["title_uk"]
            bag.title_en = data["title_en"]
            bag.description_uk = data["description_uk"]
            bag.description_en = data["description_en"]
            bag.feature_1_uk = data["feature_1_uk"]
            bag.feature_1_en = data["feature_1_en"]
            bag.feature_2_uk = data["feature_2_uk"]
            bag.feature_2_en = data["feature_2_en"]
            bag.feature_3_uk = data["feature_3_uk"]
            bag.feature_3_en = data["feature_3_en"]
            bag.is_active = True
            bag.save()

        self.stdout.write(self.style.SUCCESS("✓ BagType seeded"))

    def _seed_flexo_section(self):
        flexo, _ = FlexoSection.objects.get_or_create(pk=1)
        flexo.title_uk = "Флексодрук на плівці"
        flexo.title_en = "Flexoprinting on film"
        flexo.lead_text_uk = "Флексографія — найпоширеніший метод нанесення зображення на пакувальні матеріали в рулонах. Ми друкуємо на поліетилені, поліпропілені та будь-якій гнучкій плівці."
        flexo.lead_text_en = "Flexography is the most common method of applying images to packaging materials in rolls. We print on polyethylene, polypropylene and any flexible film."
        flexo.body_text_uk = "Результат — інформативна, барвиста й економна упаковка, яка привертає увагу і захищає товар. Метод підходить для харчової промисловості, текстилю, побутової хімії та будівельних матеріалів."
        flexo.body_text_en = "The result is informative, colorful and economical packaging that catches attention and protects the product. The method is suitable for food industry, textiles, household chemicals and building materials."
        flexo.cta_text_uk = "Замовити флексодрук"
        flexo.cta_text_en = "Order flexoprinting"
        flexo.cta_url = "#contact"
        flexo.save()

        benefits_data = [
            {
                "title_uk": "До 8 кольорів",
                "title_en": "Up to 8 colors",
                "text_uk": "Насичений колір, чіткі межі, точна передача відтінків брендової палітри.",
                "text_en": "Saturated color, sharp edges, accurate reproduction of brand palette shades.",
                "order": 1,
            },
            {
                "title_uk": "Харчова безпека",
                "title_en": "Food safety",
                "text_uk": "Водорозчинні нешкідливі фарби — сертифіковані для контакту з харчовими продуктами.",
                "text_en": "Water-soluble non-toxic inks certified for food contact.",
                "order": 2,
            },
            {
                "title_uk": "Будь-який матеріал",
                "title_en": "Any material",
                "text_uk": "LDPE, HDPE, BOPP, CPP, поліпропілен, металізована плівка — обмежень немає.",
                "text_en": "LDPE, HDPE, BOPP, CPP, polypropylene, metalized film — no limits.",
                "order": 3,
            },
            {
                "title_uk": "Економічність",
                "title_en": "Cost-effectiveness",
                "text_uk": "Тонкий шар фарби, висока швидкість тиражу — нижча ціна на великих обсягах.",
                "text_en": "Thin ink layer, high printing speed — lower price on large volumes.",
                "order": 4,
            },
        ]

        FlexoBenefit.objects.filter(flexo=flexo).delete()
        for data in benefits_data:
            benefit = FlexoBenefit.objects.create(
                flexo=flexo,
                title_uk=data["title_uk"],
                title_en=data["title_en"],
                text_uk=data["text_uk"],
                text_en=data["text_en"],
                order=data["order"],
            )

        self.stdout.write(self.style.SUCCESS("✓ FlexoSection and FlexoBenefit seeded"))

    def _seed_about_section(self):
        about, _ = AboutSection.objects.get_or_create(pk=1)
        about.title_uk = "Про корпорацію"
        about.title_en = "About the corporation"
        about.lead_text_uk = "Magnum — власне виробництво високоякісного пакування у Дніпрі. Ми контролюємо кожен етап: від підготовки макетів до укладання продукції в транспортну упаковку."
        about.lead_text_en = "Magnum is our own high-quality packaging production in Dnipro. We control every stage: from template preparation to packing products in transport packaging."
        about.body_text_uk = "Спеціалізуємося на виробництві поліетиленових і поліпропіленових пакетів, рулонної плівки, нанесенні флексодруку та розробці дизайну упаковки. Індивідуальний підхід до кожного клієнта — від мінімального тиражу до великих промислових партій."
        about.body_text_en = "We specialize in the production of polyethylene and polypropylene bags, roll film, flexoprinting and packaging design development. Individual approach to each customer — from minimum volume to large industrial batches."
        about.save()

        features_data = [
            {
                "text_uk": "Власне обладнання — без залежності від підрядників",
                "text_en": "Own equipment — no dependence on contractors",
                "order": 1,
            },
            {
                "text_uk": "Флексодрук до 8 кольорів",
                "text_en": "Flexoprinting up to 8 colors",
                "order": 2,
            },
            {
                "text_uk": "Біорозкладні матеріали у каталозі",
                "text_en": "Biodegradable materials in the catalog",
                "order": 3,
            },
            {
                "text_uk": "Доставка по всій Україні",
                "text_en": "Delivery throughout Ukraine",
                "order": 4,
            },
        ]

        AboutFeature.objects.filter(about=about).delete()
        for data in features_data:
            AboutFeature.objects.create(
                about=about,
                text_uk=data["text_uk"],
                text_en=data["text_en"],
                order=data["order"],
            )

        stats_data = [
            {
                "value_uk": "15+",
                "value_en": "15+",
                "label_uk": "Позицій в каталозі",
                "label_en": "Items in catalog",
                "order": 1,
            },
            {
                "value_uk": "100%",
                "value_en": "100%",
                "label_uk": "Власне виробництво",
                "label_en": "Own production",
                "order": 2,
            },
            {
                "value_uk": "UA",
                "value_en": "UA",
                "label_uk": "Доставка по Україні",
                "label_en": "Delivery across Ukraine",
                "order": 3,
            },
        ]

        AboutStat.objects.filter(about=about).delete()
        for data in stats_data:
            AboutStat.objects.create(
                about=about,
                value_uk=data["value_uk"],
                value_en=data["value_en"],
                label_uk=data["label_uk"],
                label_en=data["label_en"],
                order=data["order"],
            )

        self.stdout.write(self.style.SUCCESS("✓ AboutSection, AboutFeature and AboutStat seeded"))

    def _seed_testimonials(self):
        testimonials_data = [
            {
                "name": "Олена Коваленко",
                "text_uk": "Дуже задоволені якістю пакетів! Замовляємо для своєї пекарні вже більше року. Друк чіткий, доставка вчасна.",
                "text_en": "Very satisfied with the quality of the bags! We've been ordering for our bakery for over a year. The printing is clear, delivery is timely.",
                "role_uk": "Власниця пекарні",
                "role_en": "Bakery owner",
                "order": 1,
            },
            {
                "name": "ТОВ «Агро-Постач»",
                "text_uk": "Пакети поліетиленові — якість висока, витримують навантаження, не рвуться. Рекомендуємо Корпорацію Магнум як надійного партнера.",
                "text_en": "Polyethylene bags — high quality, withstand loads, do not tear. We recommend Magnum Corporation as a reliable partner.",
                "role_uk": "Партнер",
                "role_en": "Partner",
                "order": 2,
            },
            {
                "name": "Ігор Мельник",
                "text_uk": "Швидко зв'язалися, проконсультували по плівці та флексодруку. Ціни приємні, сервіс на висоті.",
                "text_en": "Got in touch quickly, consulted on film and flexoprinting. Prices are pleasant, service is top-notch.",
                "role_uk": "Менеджер із закупівель",
                "role_en": "Procurement manager",
                "order": 3,
            },
        ]

        for data in testimonials_data:
            testimonial, _ = Testimonial.objects.get_or_create(
                name=data["name"],
                defaults={"text_uk": data["text_uk"], "text_en": data["text_en"]}
            )
            testimonial.text_uk = data["text_uk"]
            testimonial.text_en = data["text_en"]
            testimonial.role_uk = data["role_uk"]
            testimonial.role_en = data["role_en"]
            testimonial.order = data["order"]
            testimonial.is_active = True
            testimonial.save()

        self.stdout.write(self.style.SUCCESS("✓ Testimonial seeded"))

    def _seed_contact_section(self):
        contact, _ = ContactSection.objects.get_or_create(pk=1)
        contact.title_uk = "Зв'яжіться з нами"
        contact.title_en = "Get in touch"
        contact.intro_text_uk = "Залиште заявку — наш менеджер зв'яжеться з вами найближчим часом і відповість на всі запитання."
        contact.intro_text_en = "Leave a request — our manager will contact you soon and answer all questions."
        contact.save()
        self.stdout.write(self.style.SUCCESS("✓ ContactSection seeded"))

    def _seed_catalog_content(self):
        catalog, _ = CatalogPageContent.objects.get_or_create(pk=1)
        catalog.title_uk = "Каталог продукції"
        catalog.title_en = "Product catalog"
        catalog.description_uk = "Власне виробництво пакувальних матеріалів — пакети, плівки, коробки. Від 1 кг до великих тиражів."
        catalog.description_en = "Own production of packaging materials — bags, films, boxes. From 1 kg to large volumes."
        catalog.hero_title_uk = "Каталог продукції"
        catalog.hero_title_en = "Product catalog"
        catalog.hero_description_uk = "Власне виробництво пакувальних матеріалів — пакети, плівки, коробки. Від 1 кг до великих тиражів."
        catalog.hero_description_en = "Own production of packaging materials — bags, films, boxes. From 1 kg to large volumes."
        catalog.order_cta_text_uk = "Замовити / Дізнатися ціну"
        catalog.order_cta_text_en = "Order / Find out price"
        catalog.product_desc_heading_uk = "Опис продукту"
        catalog.product_desc_heading_en = "Product description"
        catalog.related_heading_uk = "Схожі товари"
        catalog.related_heading_en = "Related products"
        catalog.cta_title_uk = "Не знайшли потрібне?"
        catalog.cta_title_en = "Didn't find what you need?"
        catalog.cta_description_uk = "Ми виготовляємо упаковку на замовлення за вашими розмірами та дизайном."
        catalog.cta_description_en = "We manufacture packaging to order according to your sizes and design."
        catalog.cta_button_text_uk = "Замовити індивідуально"
        catalog.cta_button_text_en = "Order individually"
        catalog.save()
        self.stdout.write(self.style.SUCCESS("✓ CatalogPageContent seeded"))

    def _seed_services_section(self):
        sec, _ = ServicesSection.objects.get_or_create(pk=1)
        sec.title_uk = "Що ми виробляємо"
        sec.title_en = "What we manufacture"
        sec.subtitle_uk = "Повний цикл виробництва — від розробки макету до доставки готової продукції"
        sec.subtitle_en = "Full production cycle — from layout development to delivery of finished products"
        sec.save()
        self.stdout.write(self.style.SUCCESS("✓ ServicesSection seeded"))

    def _seed_bags_section(self):
        sec, _ = BagsSection.objects.get_or_create(pk=1)
        sec.title_uk = "Типи пакетів"
        sec.title_en = "Types of bags"
        sec.subtitle_uk = "Виготовляємо з поліетилену (LDPE, HDPE) та поліпропілену (BOPP, CPP) — під будь-яке завдання"
        sec.subtitle_en = "Made from polyethylene (LDPE, HDPE) and polypropylene (BOPP, CPP) — for any task"
        sec.save()
        self.stdout.write(self.style.SUCCESS("✓ BagsSection seeded"))

    def _seed_catalog_preview_section(self):
        sec, _ = CatalogPreviewSection.objects.get_or_create(pk=1)
        sec.title_uk = "Популярна продукція"
        sec.title_en = "Popular products"
        sec.subtitle_uk = "Замовляйте безпосередньо у виробника — без посередників"
        sec.subtitle_en = "Order directly from the manufacturer — without middlemen"
        sec.cta_button_text_uk = "Весь каталог"
        sec.cta_button_text_en = "Full catalog"
        sec.save()
        self.stdout.write(self.style.SUCCESS("✓ CatalogPreviewSection seeded"))

    def _seed_currency_section(self):
        sec, _ = CurrencySection.objects.get_or_create(pk=1)
        sec.title_uk = "Курс валют"
        sec.title_en = "Exchange rates"
        sec.subtitle_uk = "Офіційний курс Національного банку України"
        sec.subtitle_en = "Official rate of the National Bank of Ukraine"
        sec.save()
        self.stdout.write(self.style.SUCCESS("✓ CurrencySection seeded"))

    def _seed_testimonials_section(self):
        sec, _ = TestimonialsSection.objects.get_or_create(pk=1)
        sec.title_uk = "Відгуки клієнтів"
        sec.title_en = "Customer reviews"
        sec.save()
        self.stdout.write(self.style.SUCCESS("✓ TestimonialsSection seeded"))

    def _seed_company_info_extra(self):
        company, _ = CompanyInfo.objects.get_or_create(pk=1)
        if not company.postal_code:
            company.postal_code = "49102"
        if not company.street_address:
            company.street_address_uk = "вул. Волинська, 46"
            company.street_address_en = "46 Volynska St"
        company.save()
        self.stdout.write(self.style.SUCCESS("✓ CompanyInfo extra fields seeded"))
