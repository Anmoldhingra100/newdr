# Generated by Django 5.0.6 on 2024-07-30 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solar_app', '0007_alter_mysolarrr_bkk_alter_mysolarrr_production_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mysolarrr',
            name='bkk',
            field=models.IntegerField(max_length=4),
        ),
        migrations.AlterField(
            model_name='mysolarrr',
            name='production',
            field=models.IntegerField(max_length=4),
        ),
        migrations.AlterField(
            model_name='mysolarrr',
            name='total',
            field=models.IntegerField(max_length=4),
        ),
    ]