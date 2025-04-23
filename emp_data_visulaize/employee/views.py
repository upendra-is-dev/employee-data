from rest_framework import viewsets
from .models import Department, Employee, Attendance, PerformanceRecord
from .serializers import DepartmentSerializer, EmployeeSerializer, AttendanceSerializer, PerformanceRecordSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Avg, Count

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class PerformanceRecordViewSet(viewsets.ModelViewSet):
    queryset = PerformanceRecord.objects.all()
    serializer_class = PerformanceRecordSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def summary(request):
    avg_score = PerformanceRecord.objects.aggregate(avg_score=Avg('score'))
    attendance_count = Attendance.objects.values('status').annotate(count=Count('id'))
    return Response({
        'average_score': avg_score['avg_score'],
        'attendance_summary': attendance_count
    })