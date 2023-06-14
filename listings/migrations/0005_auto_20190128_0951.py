# Generated by Django 2.1 on 2019-01-28 04:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_listing_types'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='build_year',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='listing',
            name='rate',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]