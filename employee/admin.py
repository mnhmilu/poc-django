

# Register your models here.
from django.contrib import admin
from .models import Employee,Project,Event


class ProjectAdmin(admin.ModelAdmin):
    search_fields = ["team_lead", "due_date"]
    list_filter = ("due_date",)

admin.site.register(Employee)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Event)

