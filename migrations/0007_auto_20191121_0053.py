# Generated by Django 2.2.6 on 2019-11-20 18:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('educate', '0006_auto_20191121_0028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(default='index', max_length=100)),
                ('number_of_clicks', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='author',
            name='DOR',
            field=models.DateField(default=datetime.datetime(2019, 11, 20, 18, 53, 27, 14980, tzinfo=utc)),
        ),
    ]
