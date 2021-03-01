"""BPIBS12 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from student.views import *
from officer.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),

                  path('Register', student_register, name='studentadd'),
                  path('Student_Login', stud_log, name='studlog'),
                  path('Student_Dashboard', show_studentdata, name='studdata'),
                  path('Student_Dashboard/Notifications', show_not, name='shownot'),
                  path('Update_Details', stud_upd, name='update'),
                  path('Student_Logout', stud_out),

                  path('Officer_Login', officer_log, name='offlog'),
                  path('Officer_Dashboard', off_data, name='offdashBOARD'),
                  path('Officer_Logout', off_out),
                  path('Students_Data', officer_studentdata, name='offdash'),
                  path('Add_Notification', add_not, name='addnot'),
                  path('Add_Notification/update/<n_id>', edit, name='not_edit'),
                  path('Add_Notification/delete/<n_id>', remove, name='not_del'),

                  path('Students_Data/<rid>', stud_view, name='sview'),

                  path('Recruiters_Contact', rec_register, name='recadd'),

                  path('', base, name='base'),
                  path('ContactUs', query, name='contact'),
                  path('courses/<name>', plc_home, name='plachome'),
                  path('admins', rolls, name='roll'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
