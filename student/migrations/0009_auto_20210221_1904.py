# Generated by Django 3.0.10 on 2021-02-21 13:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_auto_20210220_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='d_o_b',
            field=models.DateField(default=datetime.datetime(2021, 2, 21, 13, 34, 43, 483841, tzinfo=utc)),
        ),
    ]
