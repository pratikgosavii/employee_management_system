from django.db import models

# Create your models here.



from users.models import User
from datetime import datetime, timezone
from store.models import *






class employee_allowance(models.Model):

    employee = models.ForeignKey(employee, on_delete=models.CASCADE, related_name = 'employee_allo')
    allowance = models.ForeignKey(allowance , on_delete=models.CASCADE)
    description = models.CharField(max_length=120, unique=False)
    status = models.CharField(choices = status_choice, max_length=120)
    amount = models.FloatField()


    def __str__(self):

        return self.allowance.name
    

class employee_deduction(models.Model):

    employee = models.ForeignKey(employee, on_delete=models.CASCADE, related_name = 'employee_dedu')
    deduction = models.ForeignKey(deduction, on_delete=models.CASCADE)
    description = models.CharField(max_length=120, unique=False)
    status = models.CharField(choices = status_choice, max_length=120)
    amount = models.FloatField()

   
    def __str__(self):

        return self.employee.name
    

class employee_loan(models.Model):

    employee = models.ForeignKey(employee, on_delete=models.CASCADE, related_name = 'employee_loan_re')
    loan = models.ForeignKey(loan, on_delete=models.CASCADE)
    total_loan_amount = models.FloatField()
    loan_percentage = models.BigIntegerField()
    year = models.BigIntegerField()
    emi = models.BigIntegerField()
    description = models.CharField(max_length=120, unique=False)
    status = models.CharField(choices = status_choice, max_length=120)
    amount = models.FloatField(null = True, blank = True)
    loan_from = models.DateField(auto_now_add=False, default = datetime.now(), blank = True, null = True)
    loan_to = models.DateField(auto_now_add=False, default = datetime.now(), blank = True, null = True)

    def __str__(self):

        return self.employee.name
    

class employee_miscellaneous_deduction(models.Model):

    employee = models.ForeignKey(employee, on_delete=models.CASCADE, related_name = 'employee_misc')
    miscellaneous = models.ForeignKey(miscellaneous_deduction, on_delete=models.CASCADE)
    description = models.CharField(max_length=120, unique=False)
    status = models.CharField(choices = status_choice, max_length=120)
    date = models.DateTimeField(auto_now=False)


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
    old_basic = models.FloatField()
    new_basic = models.FloatField()
    description = models.CharField(max_length=120, unique=False)
    status = models.CharField(choices = status_choice, max_length=120)
    incerement_date = models.DateField(auto_now_add=False, default = datetime.now(), blank = True, null = True)

    def __str__(self):

        return self.department.name


leave_choice =(
    ("medical_leave", "Medical Leave"),
    ("earned_leave", "Earned Leave"),
    ("marriage_leave" , "Marriage Leave"),
    ("paternity_leave", "Paternity Leave"),
   
)

class leaves(models.Model):

    employee = models.ForeignKey(employee, on_delete=models.CASCADE)
    date_from =  models.DateField(auto_now_add=False, default = datetime.now(), blank = True, null = True)
    date_to =  models.DateField(auto_now_add=False, default = datetime.now(), blank = True, null = True)
    total_days =  models.IntegerField()
    leave_type = models.CharField(choices = leave_choice, max_length=120)
    description = models.CharField(max_length=120, unique=False)
    status = models.CharField(choices = status_choice, max_length=120)

    def __str__(self):

        return self.employee.name
    

class employee_total_leaves(models.Model):

    employee = models.ForeignKey(employee, on_delete=models.CASCADE)
    earned_leaves =  models.IntegerField(default=0)
    medical_leaves =  models.IntegerField(default=0)
    paternity_leave =  models.IntegerField(default=0)
    marriage_leave =  models.IntegerField(default=0)

    def __str__(self):

        return self.employee.name
    

class month_working_days(models.Model):

    date =  models.DateField(auto_now_add=False, default = datetime.now(), blank = True, null = True)
    working_days =  models.IntegerField()

    

from django.utils import timezone
from django.db import models, IntegrityError

class employee_salary(models.Model):


    employee = models.ForeignKey(employee, on_delete=models.CASCADE)
    is_salary_generated = models.BooleanField(blank = True, null = True)
    salary_date = models.DateField()
    deduction_amount = models.FloatField(blank = True, null = True)
    allowance_amount = models.FloatField(blank = True, null = True)
    loan_amount = models.FloatField(blank = True, null = True)
    miscellaneous_deduction_amount = models.FloatField(blank = True, null = True)
    total_salary = models.FloatField(default=timezone.now, blank = True, null = True) 

    def __str__(self):

        return self.employee.name
        
    def save(self, *args, **kwargs):
        # Check for uniqueness based on employee, salary month, salary year, and is_salary_generated
        if employee_salary.objects.filter(
            employee=self.employee,
            salary_date__month=self.salary_date.month,
            salary_date__year=self.salary_date.year,
        ).exclude(pk=self.pk).exists():
            raise IntegrityError("Duplicate entry for the same employee, month, and year.")
        
        super().save(*args, **kwargs)

    
    def __str__(self):
        return self.employee.name



