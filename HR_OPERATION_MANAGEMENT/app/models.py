from django.db import models

class Employee(models.Model):
    des = (
        ('manager', 'MANAGER'),
        ('hrhead', 'HRHEAD'),
        ('interviewer', 'INTERVIEWER'),
        ('employee', 'EMPLOYEE'),
        )
    name=models.CharField(max_length=30)
    password=models.CharField(max_length=20)
    designation=models.CharField(max_length=12,choices=des)
    address=models.CharField(max_length=50)
    contact_no=models.IntegerField()
    email=models.EmailField()
