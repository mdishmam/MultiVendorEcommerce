# Generated by Django 5.0.3 on 2024-03-26 09:21

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0008_alter_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyRevenue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('total_sell', models.FloatField(default=0)),
                ('total_buying_price', models.FloatField(default=0)),
                ('orders', models.ManyToManyField(related_name='dailyrevenue_orders', to='ecommerce.order')),
                ('user', models.ForeignKey(limit_choices_to={'type': 'seller'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
