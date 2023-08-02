from django.db import models

# Create your models here.



from users.models import User
from datetime import datetime, timezone
from store.models import *






class employee_allowance(models.Model):

    employee = models.ForeignKey(employee, on_delete=models.CASCADE)
    allowance = models.ForeignKey(allowance, on_delete=models.CASCADE)
    amount = models.BigIntegerField()
    description = models.CharField(max_length=120, unique=False)
    status = models.CharField(choices = status_choice, max_length=120)


    def __str__(self):

        return self.allowance.name
    

class employee_deduction(models.Model):

    employee = models.ForeignKey(employee, on_delete=models.CASCADE)
    deduction = models.ForeignKey(deduction, on_delete=models.CASCADE)
    amount = models.BigIntegerField()
    description = models.CharField(max_length=120, unique=False)
    status = models.CharField(choices = status_choice, max_length=120)


    def __str__(self):

        return self.employee.name
    

class employee_loan(models.Model):

    employee = models.ForeignKey(employee, on_delete=models.CASCADE)
    loan = models.ForeignKey(loan, on_delete=models.CASCADE)
    total_loan_amount = models.BigIntegerField()
    loan_percentage = models.BigIntegerField()
    year = models.BigIntegerField()
    emi = models.BigIntegerField()
    description = models.CharField(max_length=120, unique=False)
    status = models.CharField(choices = status_choice, max_length=120)


    def __str__(self):

        return self.employee.name
    

class employee_miscellaneous_deduction(models.Model):

    employee = models.ForeignKey(employee, on_delete=models.CASCADE)
    miscellaneous = models.ForeignKey(miscellaneous_deduction, on_delete=models.CASCADE)
    amount = models.BigIntegerField()
    description = models.CharField(max_length=120, unique=False)
    status = models.CharField(choices = status_choice, max_length=120)


    def __str__(self):

        return self.employee.name
    