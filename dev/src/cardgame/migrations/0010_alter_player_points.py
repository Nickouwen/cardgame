# Generated by Django 4.1.6 on 2023-02-17 00:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cardgame", "0009_alter_card_options_remove_card_collections_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="player",
            name="points",
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
