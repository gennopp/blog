# Generated by Django 3.1 on 2020-12-16 17:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20201216_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 16, 17, 46, 52, 538510, tzinfo=utc)),
        ),
    ]
