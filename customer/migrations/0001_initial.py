# Generated by Django 4.2.1 on 2023-05-24 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Hostel",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="MenuItem",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("image", models.ImageField(upload_to="menu_images/")),
                ("price", models.DecimalField(decimal_places=2, max_digits=5)),
                (
                    "category",
                    models.ManyToManyField(related_name="item", to="customer.category"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Restaurant",
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
                ("restaurant_name", models.CharField(max_length=100)),
                ("uname", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="restaurant_images/")),
            ],
        ),
        migrations.CreateModel(
            name="Student",
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
                ("name", models.CharField(max_length=100)),
                ("roll_no", models.CharField(max_length=100)),
                ("password", models.CharField(default="CNBT", max_length=300)),
                (
                    "block",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customer.hostel",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderModel",
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
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=7)),
                ("name", models.CharField(blank=True, max_length=50)),
                ("roll_no", models.CharField(blank=True, max_length=50)),
                ("street", models.CharField(blank=True, max_length=50)),
                ("is_paid", models.BooleanField(default=False)),
                ("is_shipped", models.BooleanField(default=False)),
                ("is_delivered", models.BooleanField(default=False)),
                (
                    "items",
                    models.ManyToManyField(
                        blank=True, related_name="order", to="customer.menuitem"
                    ),
                ),
                (
                    "restaurant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customer.restaurant",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customer.student",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="menuitem",
            name="restaurant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="customer.restaurant"
            ),
        ),
    ]
