from django.contrib import admin
from sql.models import Student
class StudentAdmin(admin.ModelAdmin):
    list_display=('name','number','sex','date')
    list_filter=('sex',)
    search_fields=('sex',)
    ordering=('number',)
admin.site.register(Student,StudentAdmin)
# Register your models here.
