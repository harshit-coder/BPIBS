from django.forms import ModelForm
from django import forms
from django.forms import ModelChoiceField
from .models import *
from django.core import validators
from .views import *


class StudentForm(ModelForm):
    labels = {'s_name': "* Name", 'Univroll': "* University Roll No", 's_phone_no': "* Mobile No.",
              'alt_phone': "* Alternate Mobile No", 's_email_id': "* Email Id", ' d_o_b': "* Date Of Birth",
              'c_name': "* Choose your Course", 'btch_start': "* Batch Start:", 'btch_end': "* Batch End:",
              'sch_name': "* School Name", 'sch_per': "* 12th Percentage",
              'grad_name': "* Graduation College Name(If)", 'grad_per': "* Graduation Percentage(If)",
              'other_skills': "Any Other Skills", 'field': "Your Field Of Interest:",
              'projects': "Worked Or Working on Any projects(If)",
              'any_internships': "Done or Doing any Internship(If)"}
    s_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': "FirstName  LastName.", 'style': "background-color: #dadada"}),
        max_length=100,
        validators=[validators.RegexValidator('[a-zA-Z\s]+$', "Only Alphabets are allowed in name")],
        error_messages={"required": "Only alphabets are allowed"},
        required=True)
    Univroll = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': "form-control", 'placeholder': "Enter your University Roll no.",
               'style': "background-color: #dadada"}),
        validators=[validators.MinValueValidator(1, "University Roll no not less than 1")],
        error_messages={"unique": "Someone is already "
                                  "registered in this "
                                  "roll no.",
                        "required": "Your Roll Number is "
                                    "not in database"},
        required=True)
    s_phone_no = forms.CharField(widget=forms.NumberInput(
        attrs={'class': "form-control", 'placeholder': "Enter your mobile number.",
               'style': "background-color: #dadada"}),
        validators=[validators.MinLengthValidator(10, "Mobile number should be of 10 digit"),
                    validators.MaxLengthValidator(10, "Mobile number should be of 10 digits")],
        error_messages={"unique": "Someone phone with this phone No. already registered",
                        "required": "mobile no. should be of 10 digits and unique"},

        required=True)
    alt_phone = forms.CharField(widget=forms.NumberInput(
        attrs={'class': "form-control", 'placeholder': "Enter a alternate mobile number",
               'style': "background-color: #dadada"}), validators=[validators.MinLengthValidator(10, "Mobile number "
                                                                                                     "should be of "
                                                                                                     "10 digit"),
                                                                   validators.MaxLengthValidator(10,
                                                                                                 "Mobile number "
                                                                                                 "should be of 10 "
                                                                                                 "digits")],
        error_messages={"unique": " Someone with this alternative phone no. already registered ",
                        "required": "Mobile No. should be of 10 digits and unique"}, required=True)

    s_email_id = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': "form-control", 'placeholder': "Enter your email id", 'style': "background-color: #dadada"}),
        max_length=254, required=True)
    d_o_b = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date', 'class': "form-control", 'placeholder': "Enter date of birth",
               'style': "background-color: #dadada"}), required=True)
    c_name = forms.ModelChoiceField(
        widget=forms.Select(attrs={'class': "form-control", 'style': "background-color: #dadada"}),
        queryset=course.objects.all(), required=True)
    btch_start = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': "form-control", 'placeholder': "Enter starting year of your batch",
               'style': "background-color: #dadada"}), min_value=2010, max_value=2995, required=True)
    btch_end = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': "form-control", 'placeholder': "Enter ending year of your batch",
               'style': "background-color: #dadada"}), min_value=2010, max_value=2999, required=True)
    sch_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': "Enter your school name:",
               'style': "background-color: #dadada"}), max_length=100, required=False)
    grad_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': "Enter Yor Graduation College Name (if Studying in Pg courses) ",
               'style': "background-color: #dadada"}), max_length=100,
        help_text="For Ug students please write Pursuing", required=True)
    sch_per = forms.DecimalField(widget=forms.NumberInput(
        attrs={'class': "form-control", 'placeholder': "Your 12 th grade percentage",
               'style': "background-color: #dadada"}), max_value=100, min_value=0, max_digits=4, decimal_places=2,
        required=True)
    grad_per = forms.DecimalField(widget=forms.NumberInput(
        attrs={'class': "form-control", 'placeholder': "If CGPA then CGPA*9.5", 'style': "background-color: #dadada"}),
        max_value=100, min_value=0, max_digits=4, decimal_places=2,
        help_text="For Ug students please write 0.0", required=True)
    other_skills = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': "Enter  other skills you learned or learning",
               'style': "background-color: #dadada"}), max_length=100, required=False)
    projects = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control", 'rows': "3",
                                                            'placeholder': "Tell Us About your past projects  or "  "projects you are working on",
                                                            'style': "background-color: #dadada"}), required=False)
    field = forms.CharField(widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': "3", 'placeholder': "Tell Us About  your field of interest",
               'style': "background-color: #dadada"}), required=False)
    any_internships = forms.CharField(widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': "3", 'placeholder': "Tell Us you have done or doing any internships",
               'style': "background-color: #dadada"}), required=False)

    class Meta:
        model = student
        fields = "__all__"


class recruiterform(ModelForm):
    class Meta:
        model = recruiter_create
        fields = "__all__"
        labels = {'company_name': "Your Company Name", 'company_phone': "Mobile No.", 'company_email': "Email Id",
                  'company_det': "Write something about your company", 'url_linked_in': "Linkedin url of your company"}
        company_name = forms.CharField(max_length=100, required=True)
        company_phone = forms.CharField(error_messages={"required": "Mobile No. should be of 10 digits"}, validators=[
            validators.MinLengthValidator(10, "Mobile number should be of 10 digit"),
            validators.MaxLengthValidator(10, "Mobile number should be of 10 digits")],
                                        required=True)
        company_email = forms.EmailField(max_length=254, required=True)
        company_det = forms.CharField(required=False)
        url_linked_in = forms.URLField(validators=[
            validators.URLValidator(regex="/http(s)?:\/\/([\w]+\.)?linkedin\.com\/in\/[A-z0-9_-]+\/?/gm",
                                    message="Please enter valid Linked in URL")], required=True)
        widgets = {
            'company_name': forms.TextInput(attrs={'class': "form-control", 'placeholder': "Enter your company Name",
                                                   'style': "background-color: #dadada"}),
            'company_phone': forms.NumberInput(
                attrs={'class': "form-control", 'placeholder': "Enter your company  Phone number.",
                       'style': "background-color: #dadada"}),
            'company_email': forms.EmailInput(
                attrs={'class': "form-control", 'placeholder': "Enter your company email id",
                       'style': "background-color: #dadada"}),
            'company_det': forms.Textarea(
                attrs={'class': "form-control", 'rows': "3", 'placeholder': "Write something about your company",
                       'style': "background-color: #dadada"}),
            'url_linked_in': forms.URLInput(attrs={'class': "form-control", 'placeholder': "Your Company Linked in URL",
                                                   'style': "background-color: #dadada"})
        }


class studentlogform(forms.Form):
    labels = {'s_username': "Enter your university phone no(user id)",
              's_password': "enter the alternate Phone no. you entered (password)"}
    s_username = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': "Enter your university roll no",
               'style': "background-color: #dadada"}), required=True)
    s_password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'class': "form-control",
               'placeholder': "Enter the alternate phone no. you entered at the time of registration.",
               'style': "background-color: #dadada"}), required=True)


class officerlogform(forms.Form):
    fields = ('o_username', 'o_password',)
    labels = {'o_username': "User id", 'o_password': "Password"}
    o_username = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': "Enter the user id", 'style': "background-color: #dadada"}),
                                 required=True)
    o_password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'class': "form-control", 'placeholder': "Enter password", 'style': "background-color: #dadada"}),
                                 required=True)


class officer_notificaton(ModelForm):
    labels = {'add_course': "Add course", 'add_notification': "Enter the message ",
              'messurl': "Any url you want to attach", 'start_batch': "Batch start year", 'end_batch': "Batch end year"}
    add_course = forms.ModelChoiceField(
        widget=forms.Select(attrs={'class': "form-control", 'style': "background-color: white"}),
        queryset=course.objects.all(), required=True)
    add_notification = forms.CharField(widget=forms.Textarea(
        attrs={'class': "form-control", 'placeholder': "Enter the message", 'style': "background-color: white"}),
        required=True)
    messurl = forms.URLField(widget=forms.URLInput(
        attrs={'class': "form-control", 'placeholder': "Any link you want to attach",
               'style': "background-color: white"}), required=False)
    start_batch = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': "form-control", 'placeholder': "Starting year of the batch",
               'style': "background-color: white"}), max_value=2995, min_value=0)
    end_batch = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': "form-control", 'placeholder': "Ending year of the batch", 'style': "background-color: white"}),
        max_value=2999, min_value=0)

    class Meta:
        model = assigned_addnot
        fields = "__all__"


class query_form(forms.ModelForm):
    labels = {'crse': "Select Your Course", 'uroll': "Enter your University Roll No.", 'nme': "Enter your name ",
              'qury': "Write Your Query", 'eml': "Email ID"}
    crse = forms.ModelChoiceField(widget=forms.Select(attrs={'class': "form-control", 'placeholder': "select course",
                                                             'style': "background-color: #dadada"}),
                                  queryset=course.objects.all(), required=True)
    nme = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Enter your  Name",
                                                        'style': "background-color: #dadada"}), max_length=100,
                          required=True)
    qury = forms.CharField(widget=forms.Textarea(
        attrs={'class': "form-control", 'placeholder': "Enter the message", 'style': "background-color: #dadada;"}),
        required=False)
    uroll = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': "form-control", 'placeholder': "University Roll No",
               'style': "background-color: #dadada;"}), min_value=0, required=True)
    eml = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': "form-control", 'placeholder': "enter your email id",
               'style': "background-color: #dadada;"}), required=True)

    class Meta:
        model = query
        fields = "__all__"


class rollnoform(forms.Form):
    fields = ('c_course', 'batch_s', 'batch_e', 'f_roll', 's_roll', 'l_roll', 'tots',)
    c_course = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Enter course name",
                                      'style': "background-color: #dadada"}), max_length=100, required=True)
    batch_s = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Enter start batch",
                                                            'style': "background-color: #dadada"}), max_length=100,
                              required=True)
    batch_e = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Enter end batch",
                                                            'style': "background-color: #dadada"}), max_length=100,
                              required=True)

    f_roll = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': "form-control", 'placeholder': "Enter First Roll no",
                                        'style': "background-color: #dadada"}),
        required=True)
    s_roll = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': "form-control", 'placeholder': "Enter the second roll no",
                                        'style': "background-color: #dadada"}),
        required=True)
    l_roll = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Enter the last roll no",
                                      'style': "background-color: #dadada"}),
        required=True)
    tots = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Enter total student in class",
                                      'style': "background-color: #dadada"}),
        required=True)
