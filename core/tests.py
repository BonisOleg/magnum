import os

from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.test import TestCase


class EnsureSuperuserCommandTests(TestCase):
    def test_skips_when_env_not_set(self):
        for key in ("DJANGO_ADMIN_USERNAME", "DJANGO_ADMIN_PASSWORD"):
            os.environ.pop(key, None)
        call_command("ensure_superuser")
        self.assertEqual(get_user_model().objects.count(), 0)

    def test_creates_superuser_when_env_set(self):
        os.environ["DJANGO_ADMIN_USERNAME"] = "admintest"
        os.environ["DJANGO_ADMIN_PASSWORD"] = "secret123"
        try:
            call_command("ensure_superuser")
        finally:
            os.environ.pop("DJANGO_ADMIN_USERNAME", None)
            os.environ.pop("DJANGO_ADMIN_PASSWORD", None)
        user = get_user_model().objects.get(username="admintest")
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.check_password("secret123"))

    def test_updates_existing_user(self):
        User = get_user_model()
        User.objects.create_user(username="admintest", password="old")
        os.environ["DJANGO_ADMIN_USERNAME"] = "admintest"
        os.environ["DJANGO_ADMIN_PASSWORD"] = "newpass"
        try:
            call_command("ensure_superuser")
        finally:
            os.environ.pop("DJANGO_ADMIN_USERNAME", None)
            os.environ.pop("DJANGO_ADMIN_PASSWORD", None)
        user = User.objects.get(username="admintest")
        self.assertTrue(user.check_password("newpass"))
        self.assertTrue(user.is_superuser)
