# Generated by Django 4.2.4 on 2023-08-26 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Travello", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="destination",
            name="price",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
