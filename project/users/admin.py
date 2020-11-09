from django.contrib import admin
from .models import Profile, User, Teacher, Student

admin.site.register(Profile)
admin.site.register(User)
admin.site.register(Teacher)
admin.site.register(Student)
