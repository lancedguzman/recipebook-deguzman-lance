# Generated by Django 5.1.7 on 2025-03-27 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0006_recipe_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='image',
            new_name='recipe_image',
        ),
    ]
