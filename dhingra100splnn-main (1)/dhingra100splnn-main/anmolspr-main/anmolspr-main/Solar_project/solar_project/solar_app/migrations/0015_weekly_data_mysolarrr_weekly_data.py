# Generated by Django 5.0.7 on 2024-08-01 10:05

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solar_app', '0014_rename_daily_production_mysolarrr_daily_production_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='weekly_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekly_data', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='mysolarrr',
            name='weekly_data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]