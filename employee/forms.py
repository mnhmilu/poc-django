from django import forms  
from employee.models import Employee,Project,Event  
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
       
class EventForm(forms.ModelForm):

    EVENT_NAME_CHOICES = [
        ('QA FAILED', 'QA FAILED'),
        ('API ERROR', 'API ERROR'),
         ('OTHERS', 'OTHERS'),  # Add "OTHERS" as a choice
    ]

    event_name = forms.ChoiceField(choices=EVENT_NAME_CHOICES, initial='OTHERS')
    
    class Meta:
        model = Event
        fields = ['event_date','event_name','event_remarks']          
        widgets = {
            'event_remarks': forms.Textarea(attrs={'rows': 3, 'cols': 80}),  # Customize the rows and cols as needed         
            'event_date': DateInput(),
           
        }

class EventListForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'  # Display all fields from the Event model