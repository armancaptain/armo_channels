from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Subject
from .models import *

class SubjectInline(admin.StackedInline):
    model = Subject
    can_delete = False
    verbose_name_plural = 'Subject'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (SubjectInline,)
# Register your models here.
admin.site.register(User, UserAdmin)