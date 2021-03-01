from django.shortcuts import render, redirect
from django.http import HttpResponse
from student.models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from student.forms import *
from django.contrib import messages

# Create your views here.


def officer_log(request):
    if not request.session.get('user_id', None):
        if request.method == 'POST':
            SD = officerlogform(request.POST)
            Username = request.POST['o_username']
            Password = request.POST['o_password']
            print(SD.errors)
            try:
                rec = assigned.objects.get(P_id=Username, P_password=Password)
                request.session['user_id'] = rec.id


                messages.success(request, "Successfully Logged in")
                return redirect('/Officer_Dashboard')
            except assigned.DoesNotExist:
                c = course.objects.all()
                messages.error(request, "User not found or enter correct details")
                return render(request, 'Placement_Officer.html', context={'SD': SD, 'c': c})

        else:
            SD = officerlogform()
            c = course.objects.all()
            return render(request, 'Placement_Officer.html', context={'SD': SD, 'c': c})
    else:
        messages.success(request, "Already Logged in")
        return redirect('/Officer_Dashboard')


def off_out(request):
    if not request.session.get('user_id', None):
        return redirect('/Officer_Login')
    else:
        del request.session['user_id']
        messages.success(request, "Successfully logged out")
        return redirect('/Officer_Login')


def off_data(request):
    if not request.session.get('user_id', None):
        messages.success(request, "First Log in")
        return redirect('/Officer_Login')
    else:
        f = recruiter_create.objects.all()
        return render(request, 'Officer_Dashboard.html', {'f': f})


def officer_studentdata(request):
    if not request.session.get('user_id', None):
        messages.success(request, "First Log in")
        return redirect('/Officer_Login')
    else:
        asi = assigned.objects.get(id=request.session['user_id'])
        st = student.objects.filter(c_name=asi.COURSE_name)
        print(asi.COURSE_name)
        btl = student.objects.filter(c_name=asi.COURSE_name).aggregate(Max('btch_end'))
        c = course.objects.get(cname=asi.COURSE_name)
        tyear = c.total_year

        print(btl['btch_end__max'])
        if btl['btch_end__max'] is None:
            diff = 0
        else:
            diff = btl['btch_end__max'] - tyear

        so = student.objects.filter(c_name=asi.COURSE_name).filter(btch_end__gt=diff).order_by('-btch_end')
        li = student.objects.filter(c_name=asi.COURSE_name).filter(btch_end__gt=diff).order_by('-btch_end').values_list(
            'btch_end', flat=True).distinct()
        return render(request, 'Courses_Students.html', context={'so': so, 'asi': asi, 'li': li, 'c': c})


def stud_view(request, rid):
    if not request.session.get('user_id', None):
        messages.success(request, "First Log in")
        return redirect('/Officer_Login')
    else:
        dd = student.objects.get(Univroll=rid)
        return render(request, 'Particular_Student.html', {'dd': dd})


# notification system


def add_not(request):
    if not request.session.get('user_id', None):
        messages.success(request, "First Log in")
        return redirect('/Officer_Login')
    else:
        if request.method == 'POST':
            eform = officer_notificaton(request.POST)
            print(eform.errors)
            if eform.is_valid():
                try:
                    asi = assigned.objects.get(id=request.session['user_id'])
                    eform.save()
                    messages.success(request, "Notification added")
                    return redirect('/Add_Notification')
                except:
                    messages.error(request, "enter details correctly")
                    asi = assigned.objects.get(id=request.session['user_id'])
                    btl = student.objects.filter(c_name=asi.COURSE_name).aggregate(Max('btch_end'))
                    c = course.objects.get(cname=asi.COURSE_name)
                    tyear = c.total_year
                    if btl['btch_end__max'] is None:
                        diff = 0
                    else:
                        diff = btl['btch_end__max'] - tyear

                    li = student.objects.filter(c_name=asi.COURSE_name).filter(btch_end__gt=diff).order_by(
                        '-btch_end').values_list('btch_end', flat=True).distinct()
                    edata = assigned_addnot.objects.filter(add_course=asi.COURSE_name)
                    return render(request, 'Add_Notification.html',
                                  context={'eform': eform, 'li': li, 'c': c, 'edata': edata})
            else:
                messages.error(request, "enter details correctly")
                asi = assigned.objects.get(id=request.session['user_id'])
                btl = student.objects.filter(c_name=asi.COURSE_name).aggregate(Max('btch_end'))
                c = course.objects.get(cname=asi.COURSE_name)
                tyear = c.total_year
                if btl['btch_end__max'] is None:
                    diff = 0
                else:
                    diff = btl['btch_end__max'] - tyear

                li = student.objects.filter(c_name=asi.COURSE_name).filter(btch_end__gt=diff).order_by(
                    '-btch_end').values_list('btch_end', flat=True).distinct()
                edata = assigned_addnot.objects.filter(add_course=asi.COURSE_name)
                return render(request, 'Add_Notification.html',
                              context={'eform': eform, 'li': li, 'c': c, 'edata': edata})

        eform = officer_notificaton()
        asi = assigned.objects.get(id=request.session['user_id'])
        btl = student.objects.filter(c_name=asi.COURSE_name).aggregate(Max('btch_end'))
        c = course.objects.get(cname=asi.COURSE_name)
        tyear = c.total_year

        if btl['btch_end__max'] is None:
            diff = 0
        else:
            diff = btl['btch_end__max'] - tyear

        li = student.objects.filter(c_name=asi.COURSE_name).filter(btch_end__gt=diff).order_by('-btch_end').values_list(
            'btch_end', flat=True).distinct()
        edata = assigned_addnot.objects.filter(add_course=asi.COURSE_name)
        return render(request, 'Add_Notification.html', context={'eform': eform, 'li': li, 'c': c, 'edata': edata})


def edit(request, n_id):
    if not request.session.get('user_id', None):
        messages.success(request, "First Log in")
        return redirect('/Officer_Login')
    else:
        emp = assigned_addnot.objects.get(id=n_id)
        eform = officer_notificaton(instance=emp)
        if request.method == 'POST':
            emp = assigned_addnot.objects.get(id=n_id)
            eform = officer_notificaton(request.POST, instance=emp)
            print(eform.errors)
            if eform.is_valid():
                eform.save()
                asi = assigned.objects.get(id=request.session['user_id'])
                messages.success(request, 'successfully updated')
                return redirect('/Add_Notification')
            else:
                messages.error(request, 'Enter details correctly')
                emp = assigned_addnot.objects.get(id=n_id)
                eform = officer_notificaton(instance=emp)
                asi = assigned.objects.get(id=request.session['user_id'])
                btl = student.objects.filter(c_name=asi.COURSE_name).aggregate(Max('btch_end'))
                c = course.objects.get(cname=asi.COURSE_name)
                tyear = c.total_year
                if btl['btch_end__max'] is None:
                    diff = 0
                else:
                    diff = btl['btch_end__max'] - tyear
                li = student.objects.filter(c_name=asi.COURSE_name).filter(btch_end__gt=diff).order_by(
                    '-btch_end').values_list(
                    'btch_end', flat=True).distinct()
                edata = assigned_addnot.objects.filter(add_course=asi.COURSE_name)
                return render(request, 'Add_Notification.html',
                              context={'eform': eform, 'li': li, 'c': c, 'edata': edata})


        else:
            emp = assigned_addnot.objects.get(id=n_id)
            eform = officer_notificaton(instance=emp)
            asi = assigned.objects.get(id=request.session['user_id'])
            btl = student.objects.filter(c_name=asi.COURSE_name).aggregate(Max('btch_end'))
            c = course.objects.get(cname=asi.COURSE_name)
            tyear = c.total_year
            if btl['btch_end__max'] is None:
                diff = 0
            else:
                diff = btl['btch_end__max'] - tyear
            li = student.objects.filter(c_name=asi.COURSE_name).filter(btch_end__gt=diff).order_by(
                '-btch_end').values_list(
                'btch_end', flat=True).distinct()
            edata = assigned_addnot.objects.filter(add_course=asi.COURSE_name)
            return render(request, 'Add_Notification.html', context={'eform': eform, 'li': li, 'c': c, 'edata': edata})


def remove(request, n_id):
    if not request.session.get('user_id', None):
        messages.success(request, "First Log in")
        return redirect('/Officer_Login')
    else:
        emp = assigned_addnot.objects.get(id=n_id)
        emp.delete()
        asi = assigned.objects.get(id=request.session['user_id'])
        messages.success(request, "successfully deleted")
        return redirect('/Add_Notification')


def rec_register(request):
    if request.method == "POST":
        stufrm = recruiterform(request.POST)
        print(stufrm.errors)
        if stufrm.is_valid():
            stufrm.save()
            messages.success(request, "Thanks for contacting us ")
            return redirect('/Recruiters_Contact')
        else:
            c = course.objects.all()
            messages.success(request, "please enter correct details")
            return render(request, 'Recruiters_Contact.html', context={'stufrm': stufrm, 'c': c})


    else:
        stufrm = recruiterform()
        c = course.objects.all()
        return render(request, 'Recruiters_Contact.html', context={'stufrm': stufrm, 'c': c})


def query(request):
    if request.method == "POST":
        cfrm = query_form(request.POST)
        print(cfrm.errors)
        if cfrm.is_valid():
            cfrm.save()
            messages.success(request, "we will solve your query very soon")
            return redirect('/ContactUs')
        else:
            c = course.objects.all()
            messages.success(request, " please enter correct details")
            return render(request, 'ContactUs.html', context={'cfrm': cfrm, 'c': c})



    else:
        cfrm = query_form()
        c = course.objects.all()
        return render(request, 'ContactUs.html', context={'cfrm': cfrm, 'c': c})
