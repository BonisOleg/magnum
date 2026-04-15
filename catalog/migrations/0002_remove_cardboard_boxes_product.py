# Remove «Картонні коробки на замовлення» (MAG-BOX-001) and deactivate empty korobky category.

from django.db import migrations


def remove_cardboard_boxes(apps, schema_editor):
    Product = apps.get_model("catalog", "Product")
    ProductCategory = apps.get_model("catalog", "ProductCategory")
    Product.objects.filter(slug="kartonni-korobky").delete()
    Product.objects.filter(sku="MAG-BOX-001").delete()
    ProductCategory.objects.filter(slug="korobky").update(is_active=False)


def noop_reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(remove_cardboard_boxes, noop_reverse),
    ]
