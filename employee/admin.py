

# Register your models here.
from django.contrib import admin
from .models import Employee,Project

admin.site.register(Employee)
admin.site.register(Project)