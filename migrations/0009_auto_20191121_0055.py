# Generated by Django 2.2.6 on 2019-11-20 18:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('educate', '0008_auto_20191121_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='DOR',
            field=models.DateField(default=datetime.datetime(2019, 11, 20, 18, 55, 44, 636495, tzinfo=utc)),
        ),
    ]
