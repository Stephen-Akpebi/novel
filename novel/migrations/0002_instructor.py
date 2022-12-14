# Generated by Django 4.1.2 on 2022-12-06 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("novel", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Instructor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(blank=True, upload_to="users/%Y/%m/%d/")),
                ("title", models.CharField(max_length=200)),
                ("name", models.CharField(max_length=200, unique=True)),
                ("about", models.CharField(max_length=200)),
            ],
        ),
    ]
