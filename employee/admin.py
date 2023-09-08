

# Register your models here.
from django.contrib import admin
from .models import Employee,Project,Event

admin.site.register(Employee)
admin.site.register(Project)
admin.site.register(Event)