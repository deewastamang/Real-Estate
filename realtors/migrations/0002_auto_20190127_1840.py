# Generated by Django 2.1 on 2019-01-27 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='is_som',
            field=models.BooleanField(default=False, help_text='Is Seller of The Month'),
        ),
    ]
