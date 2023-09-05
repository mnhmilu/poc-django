from django.shortcuts import render, redirect  
from employee.forms import EmployeeForm  
from employee.models import Employee  
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import csv
import logging
from django.http import HttpResponse
# Create your views here.  

logger = logging.getLogger(__name__)

def home(request):
    return render(request,"dashboard.html");

@login_required
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

@login_required
def show(request):  
    employees = Employee.objects.all()  
    return render(request,"employee/show.html",{'employees':employees})  

@login_required
def edit(request, id):  
    logger.info("employee-->edit called------------->");
    employee = Employee.objects.get(id=id)  
    return render(request,'employee/edit.html', {'employee':employee})  

@login_required
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/employee/show")  
    return render(request, 'employee/edit.html', {'employee': employee})  

@login_required
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/employee/show")  
@login_required
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

from django.http import HttpResponse
from reportlab.pdfgen import canvas

@login_required
def export_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="mydata.pdf"'

    # Create the PDF object, using the response object as its "file."fffhhh
    p = canvas.Canvas(response)

    # Define the width and height of each row in the table
    row_height = 20
    column_width = 150

    # Define the data to be printed in the table
    data = [
        ['ID', 'Name', 'Email'],
    ]
    for obj in Employee.objects.all():
        data.append([obj.eid, obj.ename, obj.eemail])

    # Define border settings
    border_color = (0, 0, 0)  # Black
    border_width = 1

    # Draw the table with borders
    x = 50
    y = 750
    for row in data:
        for item in row:
            # Draw the cell border
            p.rect(x, y, column_width, -row_height, stroke=1, fill=0)
            p.drawString(x + 2, y - 12, str(item))  # Add 2 to x for padding
            x += column_width
        x = 50
        y -= row_height

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    return response

@login_required
def employee_lookup(request):
    ename_query = request.GET.get('ename', '')

    logger.warning("-------------> Employee lookup called")

    # Assuming you want to display 10 employees per page
    employees = Employee.objects.filter(ename__icontains=ename_query)
    paginator = Paginator(employees, 5)  # 10 employees per page

    page_number = request.GET.get('page')
    employees = paginator.get_page(page_number)
    return render(request, 'employee/show.html', {'employees': employees})


@login_required
def reload_view(request):
  return redirect('/employee/show')