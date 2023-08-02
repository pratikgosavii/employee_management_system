from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import *


admin.site.register(employee_allowance)
admin.site.register(employee_deduction)
admin.site.register(employee_loan)
admin.site.register(employee_miscellaneous_deduction)
