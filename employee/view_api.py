from rest_framework import generics, permissions, filters
from .models import Project, AccessAudit
from .serializers import ProjectSerializer, AccessAuditSerializer
from django.db.models import Count, F

class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.values('project_status').annotate(total=Count('project_status')).order_by()
    serializer_class = ProjectSerializer

