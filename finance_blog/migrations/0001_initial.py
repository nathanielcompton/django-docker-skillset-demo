# Generated by Django 3.0.3 on 2020-02-17 19:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("body", models.TextField()),
                ("headline", models.TextField()),
                ("promo", models.TextField(blank=True)),
                ("byline", models.CharField(max_length=255)),
                (
                    "article_type",
                    models.CharField(
                        choices=[
                            ("article", "Article"),
                            ("10-promise-series", "10 Promise Series"),
                        ],
                        default="article",
                        max_length=255,
                    ),
                ),
                ("featured_image_url", models.URLField()),
                ("featured_image_name", models.TextField(blank=True, null=True)),
                ("static_page", models.BooleanField(default=False)),
                ("path", models.TextField(unique=True)),
                ("created", models.DateTimeField()),
                ("publish_at", models.DateTimeField()),
                ("modified", models.DateTimeField()),
                ("disclosure", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("username", models.CharField(max_length=255, unique=True)),
                ("byline", models.CharField(max_length=255)),
                (
                    "contributor_type",
                    models.CharField(
                        choices=[
                            ("individual", "Individual"),
                            ("company", "Company"),
                            ("sponsor", "Sponsor"),
                            ("staff", "Staff"),
                        ],
                        default="individual",
                        max_length=255,
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("fool_uid", models.BigIntegerField(unique=True)),
                ("primary", models.BooleanField(default=False)),
                (
                    "small_avatar_url",
                    models.URLField(
                        default="http://g.foolcdn.com/avatar/1593347483/small.ashx"
                    ),
                ),
                (
                    "large_avatar_url",
                    models.URLField(
                        default="http://g.foolcdn.com/avatar/1593347483/large.ashx"
                    ),
                ),
                (
                    "twitter_username",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("short_bio", models.TextField(blank=True, null=True)),
                ("long_bio", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Instruments",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Quote",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("company_name", models.CharField(max_length=255)),
                ("symbol", models.CharField(max_length=255)),
                (
                    "exchange",
                    models.CharField(
                        choices=[
                            ("NYSE", "NYSE"),
                            ("NASDAQ", "NASDAQ"),
                            ("NYSEMKT", "NYSE MKT"),
                            ("NASDAQOTH", "NASDAQOTH"),
                            ("UNKNOWN", "Unknown"),
                        ],
                        default="UNKNOWN",
                        max_length=255,
                    ),
                ),
                (
                    "currency_code",
                    models.CharField(
                        choices=[("USD", "USD")], default="USD", max_length=255
                    ),
                ),
                ("description", models.TextField()),
                ("current_price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("change", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "percent_change",
                    models.DecimalField(decimal_places=20, max_digits=30),
                ),
                ("website", models.URLField()),
                ("last_trade_date", models.DateTimeField()),
            ],
            options={
                "unique_together": {("symbol", "exchange", "last_trade_date")},
            },
        ),
    ]
