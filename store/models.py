from django.db import models


from users.models import User
from datetime import datetime, timezone

import pytz
ist = pytz.timezone('Asia/Kolkata')





status_choice =(
    ("1", "Active"),
    ("2", "Inactive"),
   
)

nps_dcps_choice =(
    ("1", "NPS"),
    ("2", "DCPS"),
   
)

courtesy_titles =(
    ("Mr", "Mr"),
    ("Mrs", "Mrs"),
    ("Miss", "Mrs"),
    ("Ms", "Ms"),
    ("Dr", "Dr"),
   
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

        return self.name
    






class employee(models.Model):
    
    courtesy_titles = models.CharField(choices = courtesy_titles, max_length=120, blank = True, null = True)
    name = models.CharField(max_length=120, unique=False)
    middle_name = models.CharField(max_length=120, unique=False, blank = True, null = True)
    last_name = models.CharField(max_length=120, unique=False, blank = True, null = True)
    address = models.TextField(max_length=120, unique=False, blank = True, null = True)
    city = models.CharField(max_length=120, unique=False, blank = True, null = True)
    taluka = models.CharField(max_length=120, unique=False, blank = True, null = True)
    district = models.CharField(max_length=120, unique=False, blank = True, null = True)
    state = models.CharField(max_length=120, unique=False, blank = True, null = True)
    country = models.CharField(max_length=120, unique=False, blank = True, null = True)
    pin_code = models.IntegerField(blank = True, null = True)

    adhar_card = models.IntegerField(max_length=12, unique=True, blank = True, null = True)
    pan_card = models.CharField(max_length=120, unique=True, blank = True, null = True)
    biometric_no = models.CharField(max_length=120, unique=True, blank = True, null = True)
    nps_dcps = models.CharField(choices = nps_dcps_choice, max_length=120, blank = True, null = True)

    department = models.ForeignKey(department_type, on_delete=models.CASCADE, blank = True, null = True)
    employee_type = models.ForeignKey(employee_type, on_delete=models.CASCADE, blank = True, null = True)
    grade_payment = models.ForeignKey(grade_payment, on_delete=models.CASCADE, blank = True, null = True)
    grade_pay = models.ForeignKey(grade_pay, on_delete=models.CASCADE, blank = True, null = True)

    pay_scale = models.ForeignKey(pay_scale, on_delete=models.CASCADE, blank = True, null = True)
    designation = models.ForeignKey(designation, on_delete=models.CASCADE, blank = True, null = True)
    hra = models.BooleanField(default=False, blank = True, null = True)
    ta = models.BooleanField(default=False, blank = True, null = True)
    da = models.BooleanField(default=False, blank = True, null = True)
    physical_disable = models.BooleanField(default=False, blank = True, null = True)
    basic_salary = models.FloatField(blank = True, null = True)
    date_of_birth = models.DateField(auto_now_add=False, blank = True, null = True)
    date_of_joining = models.DateField(auto_now_add=False)
    date_of_retirement = models.DateField(auto_now_add=False, default = datetime.now())

    bank_ac_no = models.IntegerField(blank = True, null = True)
    permanent_address = models.TextField(max_length=120, unique=False, blank = True, null = True)

    def __str__(self):
        return self.name



class allowance(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    percentage = models.IntegerField(blank = True, null = True)
    da_percentage = models.IntegerField(blank = True, null = True)
    amount = models.IntegerField(blank = True, null = True)
    is_fixed = models.BooleanField(default=True)
    is_dcpc = models.BooleanField(default=False)
    status = models.CharField(choices = status_choice, max_length=120, blank = True, null = True)

    def __str__(self):
        return self.name


class deduction(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    percentage = models.IntegerField(blank = True, null = True)
    da_percentage = models.IntegerField(blank = True, null = True)
    amount = models.IntegerField(blank = True, null = True)
    is_fixed = models.BooleanField(default=True)
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
