# Generated by Django 3.1.7 on 2021-06-13 06:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('my_testApp', '0007_auto_20210410_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 13, 6, 52, 4, 991632, tzinfo=utc)),
        ),
    ]