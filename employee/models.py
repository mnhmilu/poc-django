
# Create your models here.


from django.db import models  

class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)  
    class Meta:  
        managed = True
        db_table = "employee"  


class Project(models.Model):  
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=100)  
    project_status = models.CharField(max_length=100)  
    due_date=models.DateField
    revised_due_dte=models.DateField
    total_deviation_days=models.IntegerField
    team_lead=models.CharField(max_length=50)
    project_poc=models.CharField(max_length=50)
    notification_sms_recipient=models.CharField(max_length=100)
    notification_email_recipient=models.CharField(max_length=100)
    block_status=models.BooleanField(default=False)
    inserted_by=models.CharField(max_length=250)
    insert_date=models.DateTimeField(auto_now_add=True)
    updated_by=models.CharField(max_length=250)
    update_date=models.DateTimeField(auto_now_add=True)    
    remarks=models.CharField(max_length=250)
    class Meta:  
        managed = True
        db_table = "project"  