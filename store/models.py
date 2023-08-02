from django.db import models


from users.models import User
from datetime import datetime, timezone

import pytz
ist = pytz.timezone('Asia/Kolkata')





status_choice =(
    ("1", "Active"),
    ("2", "Inactive"),
   
)

class pay_scale(models.Model):

    name = models.CharField(max_length=120, unique=False)
    description = models.CharField(max_length=120, unique=False)
    status = models.CharField(choices = status_choice, max_length=120)


    def __str__(self):

        return self.name

class grade_pay(models.Model):

    name = models.CharField(max_length=120, unique=False)
    description = models.CharField(max_length=120, unique=False)
    status = models.CharField(choices = status_choice, max_length=120)


    def __str__(self):

        return self.name

class grade_payment(models.Model):

    name = models.CharField(max_length=120, unique=False)
    description = models.CharField(max_length=120, unique=False)
    status = models.CharField(choices = status_choice, max_length=120)


    def __str__(self):

        return self.name

class employee_type(models.Model):

    name = models.CharField(max_length=120, unique=False)
    description = models.CharField(max_length=120, unique=False)
    status = models.CharField(choices = status_choice, max_length=120)


    def __str__(self):

        return self.name

class department_type(models.Model):

    name = models.CharField(max_length=120, unique=False)
    description = models.CharField(max_length=120, unique=False)
    status = models.CharField(choices = status_choice, max_length=120)


    def __str__(self):

        return self.name

class designation(models.Model):

    name = models.CharField(max_length=120, unique=False)
    description = models.CharField(max_length=120, unique=False)
    status = models.CharField(choices = status_choice, max_length=120)


    def __str__(self):

        return self.name

class emp_classes(models.Model):

    name = models.CharField(max_length=120, unique=False)
    description = models.CharField(max_length=120, unique=False)
    status = models.CharField(choices = status_choice, max_length=120)


    def __str__(self):

        return self.name
    

class bank(models.Model):

    name = models.CharField(max_length=120, unique=False)
    description = models.CharField(max_length=120, unique=False)
    status = models.CharField(choices = status_choice, max_length=120)


    def __str__(self):

        return self.name
    

class loan(models.Model):

    name = models.CharField(max_length=120, unique=False)
    bank = models.ForeignKey(bank, on_delete=models.CASCADE)
    description = models.CharField(max_length=120, unique=False)
    status = models.CharField(choices = status_choice, max_length=120)


    def __str__(self):

        return self.bank.name
    






class employee(models.Model):
    
    name = models.CharField(max_length=120, unique=False)
    middle_name = models.CharField(max_length=120, unique=False)
    last_name = models.CharField(max_length=120, unique=False)
    address = models.CharField(max_length=120, unique=False)
    city = models.CharField(max_length=120, unique=False)
    taluka = models.CharField(max_length=120, unique=False)
    district = models.CharField(max_length=120, unique=False)
    state = models.CharField(max_length=120, unique=False)
    country = models.CharField(max_length=120, unique=False)
    pin_code = models.IntegerField()

    adhar_card = models.CharField(max_length=120, unique=True)
    pan_card = models.CharField(max_length=120, unique=True)
    biometric_no = models.CharField(max_length=120, unique=True)
    nps_dcps = models.CharField(max_length=120, unique=True)

    department = models.CharField(max_length=120, unique=True)
    employee_type = models.ForeignKey(employee_type, on_delete=models.CASCADE)
    grade_payment = models.ForeignKey(grade_payment, on_delete=models.CASCADE)
    pay_scale = models.ForeignKey(pay_scale, on_delete=models.CASCADE)
    designation = models.ForeignKey(designation, on_delete=models.CASCADE)
    hra = models.BooleanField(default=False)
    ta = models.BooleanField(default=False)
    da = models.BooleanField(default=False)
    physical_disable = models.BooleanField(default=False)
    grade_pay = models.ForeignKey(grade_pay, on_delete=models.CASCADE)
    basic_salary = models.IntegerField()
    date_of_birth = models.DateField(auto_now_add=False)
    date_of_joining = models.DateField(auto_now_add=False)
    date_of_retirement = models.DateField(auto_now_add=False, default = datetime.now())

    bank_ac_no = models.IntegerField()
    permanent_address = models.CharField(max_length=120, unique=True)


    def __str__(self):
        return self.name



class allowance(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    percentage = models.IntegerField()
    da_percentage = models.IntegerField()
    amount = models.IntegerField()
    is_fixed = models.BooleanField(default=False)
    is_dcpc = models.BooleanField(default=False)
    status = models.CharField(choices = status_choice, max_length=120)

    def __str__(self):
        return self.name


class deduction(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    percentage = models.IntegerField()
    da_percentage = models.IntegerField()
    amount = models.IntegerField()
    is_fixed = models.BooleanField(default=False)
    is_dcpc = models.BooleanField(default=False)
    status = models.CharField(choices = status_choice, max_length=120)

    def __str__(self):
        return self.name

class miscellaneous_deduction(models.Model):

    name = models.CharField(max_length=50)
    amount = models.IntegerField()
    description = models.CharField(max_length=50)
    status = models.CharField(choices = status_choice, max_length=120)

    def __str__(self):
        return self.name
