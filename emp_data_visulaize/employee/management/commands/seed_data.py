from django.core.management.base import BaseCommand
from employee.models import Department, Employee, Attendance, PerformanceRecord
from django.contrib.auth.models import User
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Seed the database with sample employee data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create a few departments
        departments = [Department.objects.create(name=fake.job()) for _ in range(3)]

        for i in range(5):  # Create 5 employees and linked Django users
            dept = random.choice(departments)
            name = fake.name()
            email = fake.email()
            position = fake.job()
            date_joined = fake.date_this_decade()

            # Create a user account with a fixed password
            username = f"user{i}"
            password = "test1234"  # You can change this globally if needed
            user = User.objects.create_user(username=username, email=email, password=password)

            # Create employee record
            emp = Employee.objects.create(
                name=name,
                email=email,
                department=dept,
                position=position,
                date_joined=date_joined
            )

            # Generate attendance and performance records
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

            # Output credentials for testing
            print(f"[CREATED] Username: {username} | Email: {email} | Password: {password}")
