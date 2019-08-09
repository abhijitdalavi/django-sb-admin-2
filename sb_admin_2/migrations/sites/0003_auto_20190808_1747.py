# Generated by Django 2.2.4 on 2019-08-08 17:47

from django.db import migrations


def insert_sites(apps, schema_editor):
    Site = apps.get_model("sites", "Site")
    Site.objects.all().delete()

    Site.objects.create(
        id=1, domain="django-sb-admin-2.herokuapp.com", name="django-sb-admin-2"
    )


class Migration(migrations.Migration):

    dependencies = [("sites", "0002_alter_domain_unique")]

    operations = [migrations.RunPython(insert_sites)]
