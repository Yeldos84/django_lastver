# Generated by Django 5.0.6 on 2024-08-22 07:43

import datetime
import django.contrib.postgres.fields
import django.contrib.postgres.fields.ranges
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kaspi', '0004_good_reserving'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='array_field',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), default=[], size=None),
        ),
        migrations.AlterField(
            model_name='good',
            name='reserving',
            field=django.contrib.postgres.fields.ranges.DateTimeRangeField(default=(datetime.datetime(2024, 8, 22, 12, 43, 47, 524281), '2024-12-31'), verbose_name='Reserving time'),
        ),
    ]
