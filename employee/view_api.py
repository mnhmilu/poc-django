from rest_framework import generics
from .models import Project
from .serializers import ProjectSerializer
from django.db.models import Count, F

class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.values('project_status').annotate(total=Count('project_status')).order_by()
    serializer_class = ProjectSerializer