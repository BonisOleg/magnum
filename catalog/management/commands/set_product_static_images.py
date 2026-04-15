"""
Обнуляє поле product.image (Cloudinary) для товарів зі статичним WebP-зображенням,
щоб get_display_image_path() повернув шлях до static/img/*.webp.

Запуск: python3 manage.py set_product_static_images
"""
import logging
from django.core.management.base import BaseCommand
from catalog.models import Product
from catalog.constants import PRODUCT_STATIC_IMAGE_FILENAME

logger = logging.getLogger(__name__)

SLUGS_WITH_STATIC = [slug for slug, fname in PRODUCT_STATIC_IMAGE_FILENAME.items() if fname]


class Command(BaseCommand):
    help = "Clear product.image (Cloudinary) for products that have a static WebP fallback."

    def handle(self, *args, **options):
        updated = 0
        skipped = 0

        for slug in SLUGS_WITH_STATIC:
            try:
                product = Product.objects.get(slug=slug)
            except Product.DoesNotExist:
                self.stdout.write(self.style.WARNING(f"  Not found in DB: {slug}"))
                skipped += 1
                continue

            if product.image:
                product.image = None
                product.save(update_fields=["image"])
                self.stdout.write(f"  Cleared Cloudinary image: {slug}")
                updated += 1
            else:
                self.stdout.write(f"  Already empty (static fallback ready): {slug}")

        self.stdout.write(
            self.style.SUCCESS(
                f"\nDone. Updated: {updated}, skipped/not found: {skipped}."
            )
        )
