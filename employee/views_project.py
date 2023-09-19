from django.shortcuts import render, redirect  ,get_object_or_404
from employee.forms import ProjectForm,EventForm,EventListForm  
from employee.models import Project,Event  
from django.http import HttpResponse
from django.contrib import messages
from reportlab.pdfgen import canvas
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import csv
import logging
from django.http import HttpResponse
from django.utils.dateformat import format

from reportlab.lib.pagesizes import letter,landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from .choices import PROJECT_STATUS_CHOICES,EVENT_NAME_CHOICES

# Create your views here.  

logger = logging.getLogger(__name__)

# def home(request):
#     return render(request,"dashboard.html");

@login_required
def add(request):  

    logger.info("proj------------> called");
    if request.method == "POST":  
        form = ProjectForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/project/index')  
            except:  
                pass  
        else:            
            messages.error(request,form.errors)  
    else:  
        form = ProjectForm()  
    return render(request,'project/add.html',{'form':form})  

@login_required
def show(request):  
    projects = Project.objects.all()  
    return render(request,"project/index.html",{'projects':projects})  

# @login_required
# def edit(request, id):  
#     logger.warning("edit called------------->");
#     project = Project.objects.get(project_id=id)  

#     if project.total_deviation_days is not None:
#         messages.success(request,"test"+ str(project.total_deviation_days))
#     else:
#         messages.success(request, "Total Deviation Days is empty")

#     #messages.success(request,str(project.total_deviation_days))
#     return render(request,'project/edit.html', {'project':project})  


@login_required
def edit(request, id):  
    logger.warning("edit called------------->");  

    project = get_object_or_404(Project, pk=id)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('/project/index')
    else:
        form = ProjectForm(instance=project)
    
    return render(request, 'project/edit.html', {'form': form, 'project': project})

@login_required
def update(request, id):  
    

    project = Project.objects.get(project_id=id)  
  
    form = ProjectForm(request.POST, instance = project)  

   # print("update called-------------> ",form.errors);

    if form.is_valid():  
        form.save()  
        return redirect("/project/index")
    else:
        messages.error(request,form.errors)  
    return render(request, 'project/edit.html', {'project': project})  

@login_required
def destroy(request, id):  
    project = Project.objects.get(project_id=id)  
    project.delete()  
    return redirect("/project/index")  
@login_required
def export(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="somefilename.csv"'},
    )

    emplist = Project.objects.all();
    

    writer = csv.writer(response)

    writer.writerow(["ID", "Name"])
    for project in emplist: 
       writer.writerow([project.eid, project.ename]);
   
    return response

from django.http import HttpResponse
from reportlab.pdfgen import canvas

@login_required
def export_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="mydata.pdf"'

    PROJECT_STATUS_CHOICES_DICT = dict(PROJECT_STATUS_CHOICES)

    # Create the PDF object
    pdf = SimpleDocTemplate(response, pagesize=landscape(letter))

    # Create a list of data for the table
    data = [
        ['ID', 'Project Name', 'Project Status', 'Due Date', 'Revised Due Date', 'Delayed', 'Blocked?', 'POC', 'Remarks']
    ]
    
    for obj in Project.objects.all():
        data.append([obj.project_id, obj.project_name,PROJECT_STATUS_CHOICES_DICT.get(obj.project_status, 'Unknown') , obj.due_date, obj.revised_due_date,
                     obj.total_deviation_days, obj.block_status, obj.project_poc, obj.remarks])

    # Create the table and style
    table = Table(data)
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])
    table.setStyle(style)

    # Build the PDF
    elements = []
    elements.append(table)
    pdf.build(elements)

    return response
# def export_pdf(request):
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="mydata.pdf"'

#     # Create the PDF object, using the response object as its "file."fffhhh
#     p = canvas.Canvas(response)

#     # Define the width and height of each row in the table
#     row_height = 20
#     column_width = 100

#     # Define the data to be printed in the table
#     data = [
#         ['ID', 'Project Name', 'Project Staus','Due Date', 'Revised Due Date','Delayed', 'Blocked?','POC','Remarks'],
#     ]
#     for obj in Project.objects.all():
#         data.append([obj.project_id, obj.project_name, obj.due_date,obj.revised_due_date,obj.total_deviation_days,obj.block_status,obj.project_poc,obj.remarks])

#     # Define border settings
#     border_color = (0, 0, 0)  # Black
#     border_width = 1

#     # Draw the table with borders
#     x = 50
#     y = 750
#     for row in data:
#         for item in row:
#             # Draw the cell border
#             p.rect(x, y, column_width, -row_height, stroke=1, fill=0)
#             p.drawString(x + 2, y - 12, str(item))  # Add 2 to x for padding
#             x += column_width
#         x = 50
#         y -= row_height

#     # Close the PDF object cleanly, and we're done.
#     p.showPage()
#     p.save()

#     return response

@login_required
def project_lookup(request):

    projectname_query = request.GET.get('project_name', '')
    projectstatus_query = request.GET.get('project_status', '')

    projects = Project.objects.all()

    if projectname_query:    
        projects = Project.objects.filter(project_name__icontains=projectname_query)
    
    if projectstatus_query:    
        projects = Project.objects.filter(project_status__icontains=projectstatus_query)
    

    logger.warning("-------------> project lookup called")
   
    # Assuming you want to display 10 projects per page
    
    paginator = Paginator(projects, 5)  # 10 projects per page

    page_number = request.GET.get('page')
    projects = paginator.get_page(page_number)
    form = ProjectForm() 
    return render(request, 'project/index.html', {'projects': projects, 'form':form})


@login_required
def reload_view(request):
   messages.success(request, "reload called!");
   return redirect('/project/index')

def add_event_to_project(request,id):
    project = get_object_or_404(Project, pk=id)

    if request.method == 'POST':
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            event = event_form.save(commit=False)
            event.project = project
            event.save()
            return redirect('add_event_to_project', id );
    else:
    
    # Retrieve a list of events associated with the project as a QuerySet
        events = Event.objects.filter(project=project)

    project_form = ProjectForm(instance=project)
    event_form = EventForm()

    context = {
        'project': project,
        'events': events,  # Pass the QuerySet of events to the template
        'project_form': project_form,
        'event_form': event_form,
    }
    return render(request, 'project/add_event_to_project.html', context)

@login_required
def destroy_project_event(request, id):
    event = get_object_or_404(Event, pk=id)  
    project_id=event.project_id;
    event.delete()  
    return redirect('add_event_to_project', project_id);