# Generated by Django 5.0.3 on 2024-03-24 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerce", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="type",
            field=models.CharField(
                choices=[("buyer", "Buyer"), ("seller", "Seller")], max_length=50
            ),
        ),
    ]
