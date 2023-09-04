from django.shortcuts import render, redirect  
from employee.forms import EmployeeForm  
from employee.models import Employee  
import csv
from django.http import HttpResponse
# Create your views here.  

def home(request):
    return render(request,"dashboard.html");


def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/employee/show')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'employee/index.html',{'form':form})  
def show(request):  
    employees = Employee.objects.all()  
    return render(request,"employee/show.html",{'employees':employees})  
def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'employee/edit.html', {'employee':employee})  
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/employee/show")  
    return render(request, 'employee/edit.html', {'employee': employee})  
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/employee/show")  

def export(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="somefilename.csv"'},
    )

    emplist = Employee.objects.all();

    writer = csv.writer(response)

    writer.writerow(["ID", "Name"])
    for employee in emplist: 
       writer.writerow([employee.eid, employee.ename]);
   
    return response