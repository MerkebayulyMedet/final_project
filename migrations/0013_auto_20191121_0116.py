# Generated by Django 2.2.6 on 2019-11-20 19:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('educate', '0012_auto_20191121_0108'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_date',
            field=models.DateField(default=datetime.datetime(2019, 11, 20, 19, 16, 21, 772195, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='author',
            name='DOR',
            field=models.DateField(default=datetime.datetime(2019, 11, 20, 19, 16, 21, 771194, tzinfo=utc)),
        ),
    ]