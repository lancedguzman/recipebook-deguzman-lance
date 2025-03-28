# Generated by Django 5.1.7 on 2025-03-27 02:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0004_recipeingredient_description_recipeingredient_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipeingredient',
            name='description',
        ),
        migrations.RemoveField(
            model_name='recipeingredient',
            name='image',
        ),
        migrations.CreateModel(
            name='RecipeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/images')),
                ('description', models.TextField(max_length=255)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='ledger.recipe')),
            ],
        ),
    ]
