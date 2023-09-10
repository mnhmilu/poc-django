"""crudexample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin  
from django.urls import path  
from employee import views  
from employee import views_project
from django.urls import path, include
from django.views.generic.base import TemplateView # new

urlpatterns = [  
    
    path('admin/', admin.site.urls),  
    path('dashboard/',views.home),
    
    path('project/proj', views_project.proj),  
    path('project/show', views_project.project_lookup, name='project_lookup'),
    path('project/reload/', views_project.reload_view, name='project_reload'),
    path('project/edit/<int:id>', views_project.edit),  
    path('project/update/<int:id>', views_project.update),  
    path('project/delete/<int:id>', views_project.destroy),  
    path('project/delete_event/<int:id>', views_project.destroy_project_event),  
    path('project/add_event/<int:id>/', views_project.add_event_to_project, name='add_event_to_project'),


    path('employee/emp', views.emp),  
    path('employee/export',views.export),    
    path('employee/exportpdf',views.export_pdf),    
    path('employee/edit/<int:id>', views.edit),  
    path('employee/update/<int:id>', views.update),  
    path('employee/delete/<int:id>', views.destroy),  
    path('employee/reload/', views.reload_view, name='reload'),
    path('employee/show', views.employee_lookup, name='employee_lookup'),
    
    path("accounts/", include("django.contrib.auth.urls")),  # new
    path('', TemplateView.as_view(template_name='dashboard.html'), name='dashboard')
]  