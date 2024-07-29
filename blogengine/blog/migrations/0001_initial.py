# Generated by Django 5.0.7 on 2024-07-22 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(db_index=True, max_length=150)),
                ("slug", models.SlugField(max_length=150, unique=True)),
                ("body", models.TextField(blank=True, db_index=True)),
                ("date_pub", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
