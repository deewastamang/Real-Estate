# Generated by Django 2.1 on 2019-01-27 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20190127_1840'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='realstor',
            new_name='realtor',
        ),
    ]