from django import forms  
from employee.models import Employee,Project  
from django.conf import settings

class DateInput(forms.DateInput):
    input_type = 'date'

class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__"  


class ProjectForm(forms.ModelForm):    
    class Meta:  
        model = Project  
        fields = "__all__"  
        widgets = {
            'due_date': DateInput()
        }