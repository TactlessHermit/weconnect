# Generated by Django 5.1 on 2025-01-08 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_rename_job_contact_field'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='field',
            new_name='job',
        ),
    ]
