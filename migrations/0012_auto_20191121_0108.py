# Generated by Django 2.2.6 on 2019-11-20 19:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('educate', '0011_auto_20191121_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='DOR',
            field=models.DateField(default=datetime.datetime(2019, 11, 20, 19, 8, 13, 218556, tzinfo=utc)),
        ),
    ]