# Generated by Django 3.1.7 on 2021-04-06 08:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('my_testApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_name',
            field=models.CharField(default='a', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 6, 8, 53, 34, 489332, tzinfo=utc)),
        ),
    ]
