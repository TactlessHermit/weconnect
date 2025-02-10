# Generated by Django 5.1 on 2025-02-06 14:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0008_alter_contact_user'),
        ('meetings', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='report',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.contact'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
