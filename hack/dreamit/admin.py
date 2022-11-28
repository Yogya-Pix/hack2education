from django.contrib import admin
from .models import Course, Contact, Chapters, SubCourse

# Register your models here.
admin.site.register(Course)
admin.site.register(SubCourse)
admin.site.register(Chapters)
admin.site.register(Contact)