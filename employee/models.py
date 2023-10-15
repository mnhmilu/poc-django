
# Create your models here.

from django import forms
from django.db import models  
from .choices import PROJECT_STATUS_CHOICES

class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)  
    class Meta:  
        managed = True
        db_table = "employee"  




class Project(models.Model):  
    PROJECT_STATUS = PROJECT_STATUS_CHOICES
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=100)  
    due_date = models.DateField(null=True, blank=True)
    revised_due_date = models.DateField(null=True, blank=True)
    completion_date = models.DateField(null=True, blank=True)
    total_deviation_days=models.IntegerField(default=0)
    team_lead=models.CharField(max_length=50,blank=True)
    project_poc=models.CharField(max_length=50,blank=True)
    notification_sms_recipient=models.CharField(max_length=100, blank=True)
    notification_email_recipient=models.CharField(max_length=100, blank=True)
    block_status=models.BooleanField(default=False)
    inserted_by=models.CharField(max_length=250,default="admin",blank=True)
    insert_date=models.DateTimeField(auto_now_add=True)
    updated_by=models.CharField(max_length=250,default="admin",blank=True)
    update_date=models.DateTimeField(auto_now_add=True)    
    remarks=models.CharField(max_length=250,blank=True)
    project_status = models.CharField(max_length=20, choices=PROJECT_STATUS)
    
    class Meta:  
        managed = True     
        db_table = "project"  


class Event(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='events')
    event_name = models.CharField(max_length=100)
    event_date = models.DateField()
    event_remarks=models.CharField(max_length=250,blank=True)

    class Meta:  
        managed = True     
        db_table = "project_events"  
    # Add any other fields specific to your Event model

    def __str__(self):
        return self.event_name
        