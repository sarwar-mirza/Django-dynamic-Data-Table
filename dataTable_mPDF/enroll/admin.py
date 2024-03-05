from django.contrib import admin
from enroll.models import StudentInfo
# Register your models here.
@admin.register(StudentInfo)
class StudentInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'info', 'course']
