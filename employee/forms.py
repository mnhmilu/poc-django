from django import forms  
from employee.models import Employee,Project  
from django.conf import settings

class DateInput(forms.DateInput):
    input_type = 'date'

class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__"  


PROJECT_STATUS = (
    ('initiated','INITIATED'),
    ('InDev', 'IN_DEV'),
    ('InQA','IN_QA')
  
)

class ProjectForm(forms.ModelForm):    
    class Meta:  
        model = Project  
        fields = "__all__"  
        # widget=forms.Select(choices=PROJECT_STATUS)
        widgets = {
            'due_date': DateInput(),
            'revised_due_date': DateInput()            
        }
       
        