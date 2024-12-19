# Generated by Django 5.1.4 on 2024-12-19 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0004_alter_bookinstance_options"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="author",
            index=models.Index(
                fields=["first_name"], name="catalog_aut_first_n_447838_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="author",
            index=models.Index(
                fields=["last_name"], name="catalog_aut_last_na_5ff788_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="book",
            index=models.Index(fields=["title"], name="catalog_boo_title_3a1ffe_idx"),
        ),
    ]
