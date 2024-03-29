# Generated by Django 2.2.6 on 2019-11-20 19:05

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('educate', '0009_auto_20191121_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='DOR',
            field=models.DateField(default=datetime.datetime(2019, 11, 20, 19, 5, 48, 475732, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_author', models.CharField(max_length=1000)),
                ('comment_email', models.CharField(max_length=1000)),
                ('comment_text', models.TextField(default='')),
                ('comment_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='educate.Article')),
            ],
        ),
    ]
