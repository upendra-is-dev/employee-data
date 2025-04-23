from django.core.management.base import BaseCommand
from employee.models import Department, Employee, Attendance, PerformanceRecord
from faker import Faker
import random
from datetime import timedelta, date

class Command(BaseCommand):
    help = 'Seed the database with sample employee data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        departments = [Department.objects.create(name=fake.job()) for _ in range(3)]

        for _ in range(5):
            dept = random.choice(departments)
            emp = Employee.objects.create(
                name=fake.name(),
                email=fake.email(),
                department=dept,
                position=fake.job(),
                date_joined=fake.date_this_decade()
            )
            for _ in range(5):
                Attendance.objects.create(
                    employee=emp,
                    date=fake.date_this_year(),
                    status=random.choice(['Present', 'Absent'])
                )
                PerformanceRecord.objects.create(
                    employee=emp,
                    review_date=fake.date_this_year(),
                    score=random.randint(1, 10),
                    comments=fake.sentence()
                )