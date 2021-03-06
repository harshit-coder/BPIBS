# Generated by Django 3.0.10 on 2021-02-19 14:45

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(default='course', max_length=100)),
                ('total_year', models.PositiveIntegerField(default=0)),
                ('about', models.TextField(default='')),
                ('mess', models.TextField(default=' ')),
            ],
            options={
                'db_table': 'course',
            },
        ),
        migrations.CreateModel(
            name='recruiter_create',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(default='your company-name', max_length=100)),
                ('company_phone', models.CharField(default='1234567891', max_length=10)),
                ('company_email', models.EmailField(default='abc@gmail.com', max_length=254)),
                ('company_det', models.TextField(default='about your company')),
                ('url_linked_in', models.URLField(default='https://www.linkedin.com/in/default-xxxxxxxxx/')),
                ('d', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'recruiter_create',
            },
        ),
        migrations.CreateModel(
            name='Roll_no',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.BigIntegerField(null=True)),
            ],
            options={
                'db_table': 'Roll_no',
            },
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=100)),
                ('alt_phone', models.CharField(max_length=10, unique=True)),
                ('Univroll', models.BigIntegerField(unique=True)),
                ('s_phone_no', models.CharField(max_length=10, unique=True)),
                ('s_email_id', models.EmailField(max_length=254)),
                ('btch_start', models.PositiveIntegerField()),
                ('btch_end', models.PositiveIntegerField()),
                ('d_o_b', models.DateField(default=datetime.datetime(2021, 2, 19, 14, 45, 17, 777734, tzinfo=utc))),
                ('sch_name', models.CharField(max_length=200)),
                ('grad_name', models.CharField(max_length=200)),
                ('sch_per', models.DecimalField(decimal_places=2, max_digits=4)),
                ('grad_per', models.DecimalField(decimal_places=2, max_digits=4)),
                ('other_skills', models.CharField(blank=True, max_length=500, null=True)),
                ('projects', models.TextField(blank=True, null=True)),
                ('field', models.TextField(blank=True, null=True)),
                ('any_internships', models.TextField(blank=True, null=True)),
                ('c_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.course')),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uroll', models.BigIntegerField(default=0)),
                ('nme', models.CharField(default='name', max_length=100)),
                ('qury', models.TextField(default='Write your query')),
                ('eml', models.EmailField(default='abc@gmail.com', max_length=254)),
                ('dates', models.DateTimeField(auto_now_add=True)),
                ('crse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.course')),
            ],
        ),
        migrations.CreateModel(
            name='plc_comp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_name', models.CharField(default='NULL', max_length=100)),
                ('img', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('imgurl', models.URLField(default=None)),
                ('companyfield', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.course')),
            ],
        ),
        migrations.CreateModel(
            name='graph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Batch_start', models.PositiveIntegerField(default=2000)),
                ('Batch_end', models.PositiveIntegerField(default=2003)),
                ('no_of_stud', models.PositiveIntegerField(default=0)),
                ('C_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.course')),
            ],
            options={
                'db_table': 'graph',
            },
        ),
        migrations.CreateModel(
            name='files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brochure', models.FileField(blank=True, null=True, upload_to='files/')),
                ('stulist', models.FileField(blank=True, null=True, upload_to='files/')),
                ('brochureurl', models.URLField(default=None)),
                ('stulisturl', models.URLField(default=None)),
                ('subjects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.course')),
            ],
        ),
        migrations.CreateModel(
            name='comp_graph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(default='2000', max_length=100)),
                ('company', models.CharField(default='company name', max_length=100)),
                ('cx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.course')),
            ],
        ),
        migrations.CreateModel(
            name='assigned_addnot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_notification', models.TextField()),
                ('messurl', models.URLField(default=' ')),
                ('start_batch', models.PositiveIntegerField(default=0)),
                ('end_batch', models.PositiveIntegerField(default=0)),
                ('d_te', models.DateTimeField(auto_now_add=True)),
                ('add_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.course')),
            ],
            options={
                'db_table': 'assigned_addnot',
            },
        ),
        migrations.CreateModel(
            name='assigned',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('P_name', models.CharField(max_length=100, null=True)),
                ('P_id', models.CharField(max_length=100, null=True)),
                ('P_password', models.CharField(max_length=100, null=True)),
                ('COURSE_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.course')),
            ],
            options={
                'db_table': 'assigned',
            },
        ),
    ]
