# Generated by Django 2.2.24 on 2022-12-18 08:48

from django.db import migrations


def link_owner_to_flats(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all():
        owner, created = Owner.objects.get_or_create(
            full_name=flat.owner,
            pure_phone=flat.owner_pure_phone,
        )

        if created:
            continue

        if flat in owner.flats.all():
            continue

        owner.flats.add(flat)


def move_backward(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')

    for owner in Owner.objects.all():
        owner.flats.clear()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20221218_1448'),
    ]

    operations = [
        migrations.RunPython(link_owner_to_flats, move_backward),
    ]
