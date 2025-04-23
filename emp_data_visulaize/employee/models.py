from django.db import models

# Department model represents a department in the company
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        # Return the name of the department for a readable representation
        return self.name

# Employee model represents an employee working in the company
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    date_joined = models.DateField()

    def __str__(self):
        # Return the employee's name and position for a readable representation
        return f"{self.name} - {self.position}"

# Attendance model represents an employee's daily attendance record
class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=20, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    def __str__(self):
        # Return a string representation of the employee's attendance on a specific date
        return f"{self.employee.name} - {self.status} on {self.date}"

# PerformanceRecord model stores the performance review data for an employee
class PerformanceRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    review_date = models.DateField()
    score = models.IntegerField()
    comments = models.TextField()

    def __str__(self):
        # Return a string representation of the employee's review score and date
        return f"Review for {self.employee.name} on {self.review_date} - Score: {self.score}"
