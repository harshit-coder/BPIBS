# Generated by Django 3.0.10 on 2021-02-19 14:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='d_o_b',
            field=models.DateField(default=datetime.datetime(2021, 2, 19, 14, 45, 30, 742076, tzinfo=utc)),
        ),
    ]
