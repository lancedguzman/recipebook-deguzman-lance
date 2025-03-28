# Generated by Django 5.1.7 on 2025-03-27 09:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0007_rename_image_recipe_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_image',
            field=models.ImageField(default='sinigang.jpg', upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipeimage',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_images', to='ledger.recipe'),
        ),
    ]
