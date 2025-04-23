from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, EmployeeViewSet, AttendanceViewSet, PerformanceRecordViewSet, SummaryView

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'performance', PerformanceRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('employee/summary/', SummaryView.as_view()),  # Class-based view URL
]