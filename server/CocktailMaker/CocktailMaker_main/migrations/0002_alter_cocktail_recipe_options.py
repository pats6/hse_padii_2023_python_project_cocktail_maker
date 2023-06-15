# Generated by Django 4.2.2 on 2023-06-14 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("CocktailMaker_main", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="cocktail_recipe",
            options={"verbose_name": "Коктейль", "verbose_name_plural": "Коктейли"},
        ),
        migrations.AddField(
            model_name="cocktail_recipe",
            name="proportions",
            field=models.TextField(blank="true", verbose_name="Пропорции"),
        ),
    ]