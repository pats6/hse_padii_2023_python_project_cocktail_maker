# Generated by Django 4.2.2 on 2023-06-15 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CocktailMaker_main', '0002_alter_cocktail_recipe_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cocktail_recipe',
            name='proportions',
        ),
    ]