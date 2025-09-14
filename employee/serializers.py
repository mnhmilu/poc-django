from rest_framework import serializers
from .models import Project, AccessAudit

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class AccessAuditSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source="employee.ename", read_only=True)
    employee_email = serializers.EmailField(source="employee.eemail", read_only=True)

    class Meta:
        model = AccessAudit
        fields = ["id", "employee_name", "employee_email", "login_time"]
        read_only_fields = fields