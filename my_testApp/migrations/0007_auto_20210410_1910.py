# Generated by Django 3.1.7 on 2021-04-10 13:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('my_testApp', '0006_auto_20210410_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 10, 13, 40, 31, 18031, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blog',
            name='data',
            field=models.TextField(default=''),
        ),
    ]
