from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Avg, Count
from .models import Department, Employee, Attendance, PerformanceRecord
from .serializers import DepartmentSerializer, EmployeeSerializer, AttendanceSerializer, PerformanceRecordSerializer

# Class-based viewset for Department
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]

# Class-based viewset for Employee
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

# Class-based viewset for Attendance
class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]

# Class-based viewset for PerformanceRecord
class PerformanceRecordViewSet(viewsets.ModelViewSet):
    queryset = PerformanceRecord.objects.all()
    serializer_class = PerformanceRecordSerializer
    permission_classes = [IsAuthenticated]

# Class-based APIView for summary
class SummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Calculate average performance score
        avg_score = PerformanceRecord.objects.aggregate(avg_score=Avg('score'))
        # Count of attendance by status (Present/Absent)
        attendance_count = Attendance.objects.values('status').annotate(count=Count('id'))
        return Response({
            'average_score': avg_score['avg_score'],
            'attendance_summary': attendance_count
        })