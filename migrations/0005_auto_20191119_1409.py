# Generated by Django 2.2.6 on 2019-11-19 08:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('educate', '0004_auto_20191119_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='DOR',
            field=models.DateField(default=datetime.datetime(2019, 11, 19, 8, 9, 14, 930130, tzinfo=utc)),
        ),
    ]
