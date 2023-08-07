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

    date = models.DateField()
   
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
    

class employee_department_transfer(models.Model):

    employee = models.ForeignKey(employee, on_delete=models.CASCADE, related_name="sdsdss")
    old_deparment = models.ForeignKey(department_type, on_delete=models.CASCADE, related_name="sdsdsd")
    new_deparment = models.ForeignKey(department_type, on_delete=models.CASCADE, related_name="dfdfdffs")
    transfer_date = models.DateField(auto_now_add=False, default = datetime.now(), blank = True, null = True)
    description = models.CharField(max_length=120, unique=False)
    status = models.CharField(choices = status_choice, max_length=120)


    def __str__(self):

        return self.employee.name
    





class vacancy(models.Model):

    department = models.ForeignKey(department_type, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=False)
    no_of_vacancy = models.BigIntegerField()
    description = models.CharField(max_length=120, unique=False)
    status = models.CharField(choices = status_choice, max_length=120)


    def __str__(self):

        return self.department.name


class employee_increament(models.Model):

    department = models.ForeignKey(department_type, on_delete=models.CASCADE)
    employee = models.ForeignKey(employee, on_delete=models.CASCADE)
    old_basic = models.BigIntegerField()
    new_basic = models.BigIntegerField()
    description = models.CharField(max_length=120, unique=False)
    status = models.CharField(choices = status_choice, max_length=120)
    incerement_date = models.DateField(auto_now_add=False, default = datetime.now(), blank = True, null = True)

    def __str__(self):

        return self.department.name

class leaves(models.Model):

    employee = models.ForeignKey(employee, on_delete=models.CASCADE)
    date_from =  models.DateField(auto_now_add=False, default = datetime.now(), blank = True, null = True)
    date_to =  models.DateField(auto_now_add=False, default = datetime.now(), blank = True, null = True)
    total_days =  models.IntegerField()
    description = models.CharField(max_length=120, unique=False)
    status = models.CharField(choices = status_choice, max_length=120)

    def __str__(self):

        return self.employee.name
    



class employee_salary(models.Model):


    employee = models.ForeignKey(employee, on_delete=models.CASCADE)
    department = models.ForeignKey(department_type, on_delete=models.CASCADE)
    is_salary_generated = models.BooleanField()
    salary_date = models.DateField()
