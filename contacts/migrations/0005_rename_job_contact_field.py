# Generated by Django 5.1 on 2025-01-08 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_contact_birthday_contact_experience'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='job',
            new_name='field',
        ),
    ]
