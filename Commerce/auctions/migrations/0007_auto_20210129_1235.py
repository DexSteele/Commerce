# Generated by Django 3.1.5 on 2021-01-29 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20210129_1225'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auction',
            options={'ordering': ('-end_time',)},
        ),
    ]
