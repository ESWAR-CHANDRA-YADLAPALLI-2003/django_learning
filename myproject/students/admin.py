from django.contrib import admin
from .models import Course, Student

#admin.site.register(Course)
#admin.site.register(Student)
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'course', 'marks')
    search_fields = ('name', 'email')