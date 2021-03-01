from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from student.models import *
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget

from django.contrib.auth.admin import UserAdmin


@admin.register(course)
class courseadmin(admin.ModelAdmin):
    list_display = ['cname', 'total_year']
    search_fields = ['cname']
    filter_horizontal = ()
    list_filter = ()


@admin.register(files)
class ffield(admin.ModelAdmin):
    list_display = ['subjects']



@admin.register(graph)
class graph_admin(admin.ModelAdmin):
    list_display = ['C_name', 'Batch_start', 'Batch_end', 'no_of_stud']

    filter_horizontal = ()
    list_filter = ()


@admin.register(student)
class courseadmin(admin.ModelAdmin):
    list_display = ['s_name', 'alt_phone', 's_phone_no', 'c_name', 'btch_start', 'btch_end']
    search_fields = ['s_name']
    filter_horizontal = ()
    list_filter = ()


@admin.register(assigned)
class assigned_admin(admin.ModelAdmin):
    list_display = ['COURSE_name', 'P_name']
    search_fields = ['P_name']
    filter_horizontal = ()
    list_filter = ()


admin.site.register(assigned_addnot)

admin.site.register(recruiter_create)
admin.site.register(query)


@admin.register(Roll_no)
class csvadmin(ImportExportModelAdmin):
    list_display = ['roll']
    search_fields = ['roll']
    filter_horizontal = ()
    list_filter = ()


@admin.register(plc_comp)
class plc(admin.ModelAdmin):
    list_display = ['companyfield', 'comp_name']


@admin.register(comp_graph)
class compfield(ImportExportModelAdmin):
    list_display = ['company', 'number']

