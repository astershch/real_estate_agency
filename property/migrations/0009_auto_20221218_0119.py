# Generated by Django 2.2.24 on 2022-12-17 19:19

from django.db import migrations
import phonenumbers


def normalize_phonenumbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')

    for flat in Flat.objects.all().iterator():
        if flat.owner_pure_phone:
            continue

        try:
            phonenumber = phonenumbers.parse(flat.owners_phonenumber, 'RU')

            if phonenumbers.is_valid_number(phonenumber):
                flat.owner_pure_phone = phonenumber
                flat.save()

        except phonenumbers.phonenumberutil.NumberParseException:
            continue


def move_backward(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')

    for flat in Flat.objects.all().iterator():
        flat.owner_pure_phone = None
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20221218_0109'),
    ]

    operations = [
        migrations.RunPython(normalize_phonenumbers, move_backward),
    ]
