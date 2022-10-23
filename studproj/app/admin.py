from django.contrib import admin
from .models import Student

# Register your models here.
class StudAdmin(admin.ModelAdmin):
    list_display=['ids','nm','em']
admin.site.register(Student,StudAdmin)
