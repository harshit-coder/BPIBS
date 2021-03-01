# Generated by Django 3.0.10 on 2021-02-20 05:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20210219_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='eml',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='query',
            name='nme',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='query',
            name='qury',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='recruiter_create',
            name='company_det',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='recruiter_create',
            name='company_email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='recruiter_create',
            name='company_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='recruiter_create',
            name='company_phone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='recruiter_create',
            name='url_linked_in',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='d_o_b',
            field=models.DateField(default=datetime.datetime(2021, 2, 20, 5, 41, 24, 422924, tzinfo=utc)),
        ),
    ]
