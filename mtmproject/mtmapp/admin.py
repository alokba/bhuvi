from django.contrib import admin
from .models import Student,Course

class AdminStudent(admin.ModelAdmin):
    list_display = ['sname','loc','email']

class AdminCourse(admin.ModelAdmin):
    list_display = ['cname','fee','book']

admin.site.register(Student,AdminStudent)
admin.site.register(Course,AdminCourse)



