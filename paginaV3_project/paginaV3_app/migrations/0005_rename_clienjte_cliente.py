# Generated by Django 4.2.1 on 2023-06-05 18:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('paginaV3_app', '0004_clienjte'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Clienjte',
            new_name='Cliente',
        ),
    ]
