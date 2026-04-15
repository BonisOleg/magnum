"""
One-shot fix for the live database:
- Deactivate 3 unwanted products (bags, paper, boxes)
- Deactivate korobky category
- Update all product brands to "Magnum"
- Create 3 missing products if not existing
"""
import logging
from django.core.management.base import BaseCommand
from catalog.models import ProductCategory, Product

logger = logging.getLogger(__name__)

# Products to deactivate (not our profile)
BAD_PRODUCT_SLUGS = [
    "mishky-polipropilenovi",  # Polypropylene bags
    "papirovi-pakety",          # Paper bags
    "kartonni-korobky",         # Cardboard boxes
]

# Missing products to create
MISSING_PRODUCTS = [
    {
        "slug": "pakety-z-dnom",
        "name_uk": "Пакети з дном",
        "name_en": "Bags with bottom gusset",
        "order": 7,
    },
    {
        "slug": "pakety-yevrosnlot",
        "name_uk": "Пакети з єврослотом",
        "name_en": "Bags with euro slot",
        "order": 8,
    },
    {
        "slug": "pakety-konusni",
        "name_uk": "Конусні пакети",
        "name_en": "Conical bags",
        "order": 9,
    },
]


class Command(BaseCommand):
    help = "One-shot DB fix: deactivate unwanted products, update brands to Magnum, create missing products"

    def handle(self, *args, **options):
        self.stdout.write("Fixing catalog...")

        # 1. Deactivate unwanted products
        self.stdout.write("1. Deactivating unwanted products...")
        for slug in BAD_PRODUCT_SLUGS:
            try:
                product = Product.objects.get(slug=slug)
                product.is_active = False
                product.save(update_fields=["is_active"])
                self.stdout.write(f"  ✓ Deactivated: {slug}")
            except Product.DoesNotExist:
                self.stdout.write(f"  ⊘ Not found: {slug}")

        # 2. Deactivate korobky category
        self.stdout.write("2. Deactivating korobky category...")
        try:
            korobky_cat = ProductCategory.objects.get(slug="korobky")
            korobky_cat.is_active = False
            korobky_cat.save(update_fields=["is_active"])
            self.stdout.write("  ✓ Deactivated korobky category")
        except ProductCategory.DoesNotExist:
            self.stdout.write("  ⊘ korobky category not found")

        # 3. Update all product brands to Magnum
        self.stdout.write("3. Updating all product brands to 'Magnum'...")
        count = Product.objects.exclude(brand="Magnum").update(brand="Magnum")
        self.stdout.write(f"  ✓ Updated {count} products")

        # 4. Create missing products
        self.stdout.write("4. Creating missing products...")
        try:
            pakety_cat = ProductCategory.objects.get(slug="pakety", is_active=True)
        except ProductCategory.DoesNotExist:
            self.stdout.write("  ✗ Could not find active pakety category")
            return

        for p in MISSING_PRODUCTS:
            product, created = Product.objects.get_or_create(
                slug=p["slug"],
                defaults={
                    "name": p["name_uk"],
                    "name_uk": p["name_uk"],
                    "name_en": p["name_en"],
                    "category": pakety_cat,
                    "sku": "MAG-" + p["slug"].replace("-", "")[:14].upper(),
                    "short_description": "",
                    "short_description_uk": "",
                    "short_description_en": "",
                    "description": "",
                    "description_uk": "",
                    "description_en": "",
                    "brand": "Magnum",
                    "availability": "InStock",
                    "meta_title": p["name_uk"],
                    "meta_title_uk": p["name_uk"],
                    "meta_title_en": p["name_en"],
                    "meta_description": "",
                    "meta_description_uk": "",
                    "meta_description_en": "",
                    "meta_keywords": "",
                    "meta_keywords_uk": "",
                    "meta_keywords_en": "",
                    "order": p["order"],
                    "is_active": True,
                },
            )
            status = "created" if created else "already exists"
            self.stdout.write(f"  ✓ {p['slug']}: {status}")

        self.stdout.write(self.style.SUCCESS("Done. Catalog fixed."))
