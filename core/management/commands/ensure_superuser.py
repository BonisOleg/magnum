import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = (
        "Create or update a Django superuser from DJANGO_ADMIN_USERNAME and "
        "DJANGO_ADMIN_PASSWORD. Skips if either is unset."
    )

    def handle(self, *args, **options):
        username = (os.environ.get("DJANGO_ADMIN_USERNAME") or "").strip()
        password = os.environ.get("DJANGO_ADMIN_PASSWORD") or ""

        if not username or not password:
            self.stdout.write(
                "ensure_superuser: skipped (set DJANGO_ADMIN_USERNAME and "
                "DJANGO_ADMIN_PASSWORD to enable)"
            )
            return

        User = get_user_model()
        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                "email": "",
                "is_staff": True,
                "is_superuser": True,
            },
        )
        if not created:
            user.is_staff = True
            user.is_superuser = True
        user.set_password(password)
        user.save()

        action = "created" if created else "updated"
        self.stdout.write(self.style.SUCCESS(f"ensure_superuser: superuser {action} ({username!r})"))
