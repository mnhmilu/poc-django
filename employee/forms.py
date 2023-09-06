from django import forms  
from employee.models import Employee,Project  
from django.conf import settings


class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__"  


class ProjectForm(forms.ModelForm):    
    class Meta:  
        model = Project  
        fields = "__all__"  