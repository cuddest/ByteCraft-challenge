from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import customuser, task

admin.site.register(customuser, UserAdmin)
admin.site.register(task)
