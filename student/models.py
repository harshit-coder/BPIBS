from datetime import datetime, timezone

from django.db import models
from django.utils.timezone import now


# Create your models here.


class course(models.Model):
    cname = models.CharField(max_length=100, default="course")
    total_year = models.PositiveIntegerField(default=0)
    about = models.TextField(default="", blank=True, null=True)
    mess = models.TextField(default=" ", blank=True, null=True)

    def __str__(self):
        return self.cname

    class Meta:
        db_table = 'course'


class files(models.Model):
    subjects = models.ForeignKey("course", on_delete=models.CASCADE)
    brochure = models.FileField(upload_to='files/', blank=True, null=True)
    stulist = models.FileField(upload_to='files/', blank=True, null=True)
    brochureurl = models.URLField(default=None, blank=True, null=True)
    stulisturl = models.URLField(default=None, blank=True, null=True)

    def __str__(self):
        return str(self.subjects)


    class Meta:
        db_table = 'files'


class comp_graph(models.Model):
    cx = models.ForeignKey('course', on_delete=models.CASCADE)
    number = models.CharField(max_length=100, default="2000", blank=True, null=True)
    company = models.CharField(max_length=100, default="company name", blank=True, null=True)


class graph(models.Model):
    C_name = models.ForeignKey('course', on_delete=models.CASCADE)
    Batch_start = models.PositiveIntegerField(default=2000, blank=True, null=True)
    Batch_end = models.PositiveIntegerField(default=2003, blank=True, null=True)
    no_of_stud = models.PositiveIntegerField(default=0, blank=True, null=True)

    class Meta:
        db_table = 'graph'


class Roll_no(models.Model):
    roll = models.BigIntegerField(null=True)

    class Meta:
        db_table = 'Roll_no'


class student(models.Model):
    s_name = models.CharField(max_length=100,)
    alt_phone = models.CharField(max_length=10,  unique=True)
    Univroll = models.BigIntegerField(unique=True)
    s_phone_no = models.CharField(max_length=10,unique=True)
    s_email_id = models.EmailField(max_length=254)
    c_name = models.ForeignKey('course', on_delete=models.CASCADE)
    btch_start = models.PositiveIntegerField()
    btch_end = models.PositiveIntegerField()
    d_o_b = models.DateField(default=now())
    sch_name = models.CharField(max_length=200)
    grad_name = models.CharField(max_length=200,)
    sch_per = models.DecimalField(max_digits=4, decimal_places=2)
    grad_per = models.DecimalField(max_digits=4, decimal_places=2)
    other_skills = models.CharField(max_length=500,blank=True, null=True)
    projects = models.TextField(blank=True, null=True)
    field = models.TextField(blank=True, null=True)
    any_internships = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.btch_end)

    class Meta:
        db_table = 'student'


class recruiter_create(models.Model):
    company_name = models.CharField(max_length=100)
    company_phone = models.CharField(max_length=10)
    company_email = models.EmailField(max_length=254)
    company_det = models.TextField()
    url_linked_in = models.URLField(max_length=200)
    d = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'recruiter_create'


class assigned(models.Model):
    COURSE_name = models.ForeignKey('course', on_delete=models.CASCADE)
    P_name = models.CharField(max_length=100, null=True)
    P_id = models.CharField(max_length=100, null=True)
    P_password = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.P_name)

    class Meta:
        db_table = 'assigned'


class assigned_addnot(models.Model):
    add_course = models.ForeignKey('course', on_delete=models.CASCADE)
    add_notification = models.TextField()
    messurl = models.URLField(default=" ")
    start_batch = models.PositiveIntegerField(default=0000)
    end_batch = models.PositiveIntegerField(default=0000)
    d_te = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'assigned_addnot'


class plc_comp(models.Model):
    companyfield = models.ForeignKey('course', on_delete=models.CASCADE)
    comp_name = models.CharField(max_length=100, default="NULL", blank=True, null=True)
    img = models.ImageField(upload_to='images/', blank=True, null=True)
    imgurl = models.URLField(default=None, blank=True, null=True)

class query(models.Model):
    crse = models.ForeignKey('course', on_delete=models.CASCADE)
    uroll = models.BigIntegerField(default=0)
    nme= models.CharField(max_length=100)
    qury = models.TextField()
    eml = models.EmailField()
    dates = models.DateTimeField(auto_now_add=True)
