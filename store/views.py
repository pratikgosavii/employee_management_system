from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from users.models import User
from .models import *
from .forms import *
from .models import *

from datetime import date

from datetime import datetime
from django.urls import reverse
from django.http.response import HttpResponseRedirect, JsonResponse
from django.contrib import messages


import pytz
ist = pytz.timezone('Asia/Kolkata')



def numOfDays(date1):

    dt1 = date1.split('T')

    time = dt1[1]

    dt1 = dt1[0]
    
    dt1 = dt1.split('-')
    

    year = int(dt1[0])
    month = int(dt1[1])
    day = int(dt1[2])

    date1 = datetime(year,month, day, tzinfo=ist)

    return date1




@login_required(login_url='login')
def add_pay_scale(request):
    
    if request.method == 'POST':

        forms = pay_scale_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_pay_scale')
        else:
            print(forms.errors)
            return redirect('list_pay_scale')
    
    else:

        forms = pay_scale_Form()
      
        pay_scale_data = pay_scale.objects.all()

        
        context = {
            'form': forms,
            'pay_scale_data': pay_scale_data,
        }

        return render(request, 'store/add_pay_scale.html', context)

@login_required(login_url='login')
def update_pay_scale(request, pay_scale_id):

    if request.method == 'POST':

        instance = pay_scale.objects.get(id=pay_scale_id)

        forms = pay_scale_Form(request.POST, instance = instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_pay_scale')
    
    else:

        instance = pay_scale.objects.get(id= pay_scale_id)

        

        forms = pay_scale_Form(instance = instance)

        context = {
            'form': forms,
        }

        return render(request, 'store/add_pay_scale.html', context)


@login_required(login_url='login')
def delete_pay_scale(request, pay_scale_id):
    
    pay_scale.objects.get(id=pay_scale_id).delete()

    return HttpResponseRedirect(reverse('list_pay_scale_delete'))


@login_required(login_url='login')
def list_pay_scale(request):
    
     
    data = pay_scale.objects.all().order_by('name')

    context = {
            'data': data
        }


    return render(request, 'store/list_pay_scale.html', context)



@login_required(login_url='login')
def add_grade_pay(request):
    
    if request.method == 'POST':

        forms = grade_pay_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_grade_pay')
        else:
            print(forms.errors)
            return redirect('list_grade_pay')
    
    else:

        forms = grade_pay_Form()
      
        grade_pay_data = grade_pay.objects.all()

        
        context = {
            'form': forms,
            'grade_pay_data': grade_pay_data,
        }

        return render(request, 'store/add_grade_pay.html', context)

@login_required(login_url='login')
def update_grade_pay(request, grade_pay_id):

    if request.method == 'POST':

        instance = grade_pay.objects.get(id=grade_pay_id)

        forms = grade_pay_Form(request.POST, instance = instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_grade_pay')
    
    else:

        instance = grade_pay.objects.get(id=grade_pay_id)

        

        forms = grade_pay_Form(instance = instance)

        context = {
            'form': forms,
        }

        return render(request, 'store/add_grade_pay.html', context)


@login_required(login_url='login')
def delete_grade_pay(request, company_goods_id):
    
    grade_pay.objects.get(id=company_goods_id).delete()

    return HttpResponseRedirect(reverse('list_grade_pay_delete'))


@login_required(login_url='login')
def list_grade_pay(request):
    
     
    data = grade_pay.objects.all().order_by('name')

    context = {
            'data': data
        }


    return render(request, 'store/list_grade_pay.html', context)



@login_required(login_url='login')
def add_grade_payment(request):
    
    if request.method == 'POST':

        forms = grade_payment_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_grade_payment')
        else:
            print(forms.errors)
            return redirect('list_grade_payment')
    
    else:

        forms = grade_payment_Form()
      
        grade_payment_data = grade_payment.objects.all()

        
        context = {
            'form': forms,
            'grade_payment_data': grade_payment_data,
        }

        return render(request, 'store/add_grade_payment.html', context)

@login_required(login_url='login')
def update_grade_payment(request, grade_payment_id):

    if request.method == 'POST':

        instance = grade_payment.objects.get(id=grade_payment_id)

        forms = grade_payment_Form(request.POST, instance = instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_grade_payment')
    
    else:

        instance = grade_payment.objects.get(id=grade_payment_id)

        

        forms = grade_payment_Form(instance = instance)

        context = {
            'form': forms,
        }

        return render(request, 'store/add_grade_payment.html', context)


@login_required(login_url='login')
def delete_grade_payment(request, company_goods_id):
    
    grade_payment.objects.get(id=company_goods_id).delete()

    return HttpResponseRedirect(reverse('list_grade_payment_delete'))


@login_required(login_url='login')
def list_grade_payment(request):
    
     
    data = grade_payment.objects.all().order_by('name')

    context = {
            'data': data
        }


    return render(request, 'store/list_grade_payment.html', context)



@login_required(login_url='login')
def add_employee_type(request):
    
    if request.method == 'POST':

        forms = employee_type_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_employee_type')
        else:
            print(forms.errors)
            return redirect('list_employee_type')
    
    else:

        forms = employee_type_Form()
      
        employee_type_data = employee_type.objects.all()

        
        context = {
            'form': forms,
            'employee_type_data': employee_type_data,
        }

        return render(request, 'store/add_employee_type.html', context)

@login_required(login_url='login')
def update_employee_type(request, employee_type_id):

    if request.method == 'POST':

        instance = employee_type.objects.get(id=employee_type_id)

        forms = employee_type_Form(request.POST, instance = instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_employee_type')
    
    else:

        instance = employee_type.objects.get(id=employee_type_id)

        

        forms = employee_type_Form(instance = instance)

        context = {
            'form': forms,
        }

        return render(request, 'store/add_employee_type.html', context)


@login_required(login_url='login')
def delete_employee_type(request, employee_type_id):
    
    employee_type.objects.get(id=employee_type_id).delete()

    return HttpResponseRedirect(reverse('list_employee_type_delete'))


@login_required(login_url='login')
def list_employee_type(request):
    
     
    data = employee_type.objects.all().order_by('name')

    context = {
            'data': data
        }


    return render(request, 'store/list_employee_type.html', context)


@login_required(login_url='login')
def add_department_type(request):
    
    if request.method == 'POST':

        forms = department_type_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_department_type')
        else:
            print(forms.errors)
            return redirect('list_department_type')
    
    else:

        forms = department_type_Form()
      
        department_type_data = department_type.objects.all()

        
        context = {
            'form': forms,
            'department_type_data': department_type_data,
        }

        return render(request, 'store/add_department_type.html', context)

@login_required(login_url='login')
def update_department_type(request, department_type_id):

    if request.method == 'POST':

        instance = department_type.objects.get(id=department_type_id)

        forms = department_type_Form(request.POST, instance = instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_department_type')
    
    else:

        instance = department_type.objects.get(id=department_type_id)

        

        forms = department_type_Form(instance = instance)

        context = {
            'form': forms,
        }

        return render(request, 'store/add_department_type.html', context)


@login_required(login_url='login')
def delete_department_type(request, department_type_id):
    
    department_type.objects.get(id=department_type_id).delete()

    return HttpResponseRedirect(reverse('list_department_type_delete'))


@login_required(login_url='login')
def list_department_type(request):
    
     
    data = department_type.objects.all().order_by('name')

    context = {
            'data': data
        }


    return render(request, 'store/list_department_type.html', context)


@login_required(login_url='login')
def add_designation(request):
    
    if request.method == 'POST':

        forms = designation_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_designation')
        else:
            print(forms.errors)
            return redirect('list_designation')
    
    else:

        forms = designation_Form()
      
        designation_data = designation.objects.all()

        
        context = {
            'form': forms,
            'designation_data': designation_data,
        }

        return render(request, 'store/add_designation.html', context)

@login_required(login_url='login')
def update_designation(request, designation_type_id):

    if request.method == 'POST':

        instance = designation.objects.get(id=designation_type_id)

        forms = designation_Form(request.POST, instance = instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_designation')
    
    else:

        instance = designation.objects.get(id=designation_type_id)

        

        forms = designation_Form(instance = instance)

        context = {
            'form': forms,
        }

        return render(request, 'store/add_designation.html', context)


@login_required(login_url='login')
def delete_designation(request, designation_id):
    
    designation.objects.get(id=designation_id).delete()

    return HttpResponseRedirect(reverse('list_designation_delete'))


@login_required(login_url='login')
def list_designation(request):
    
     
    data = designation.objects.all().order_by('name')

    context = {
            'data': data
        }


    return render(request, 'store/list_designation.html', context)


@login_required(login_url='login')
def add_emp_classes(request):
    
    if request.method == 'POST':

        forms = emp_classes_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_emp_classes')
        else:
            print(forms.errors)
            return redirect('list_emp_classes')
    
    else:

        forms = emp_classes_Form()
      
        emp_classes_data = emp_classes.objects.all()

        
        context = {
            'form': forms,
            'emp_classes_data': emp_classes_data,
        }

        return render(request, 'store/add_emp_classes.html', context)

@login_required(login_url='login')
def update_emp_classes(request, emp_classes_id):

    if request.method == 'POST':

        instance = emp_classes.objects.get(id=emp_classes_id)

        forms = emp_classes_Form(request.POST, instance = instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_emp_classes')
    
    else:

        instance = emp_classes.objects.get(id=emp_classes_id)

        

        forms = emp_classes_Form(instance = instance)

        context = {
            'form': forms,
        }

        return render(request, 'store/add_emp_classes.html', context)


@login_required(login_url='login')
def delete_emp_classes(request, emp_classes_id):
    
    emp_classes.objects.get(id=emp_classes_id).delete()

    return HttpResponseRedirect(reverse('list_emp_classes_delete'))


@login_required(login_url='login')
def list_emp_classes(request):
    
     
    data = emp_classes.objects.all().order_by('name')

    context = {
            'data': data
        }


    return render(request, 'store/list_emp_classes.html', context)



from datetime import datetime
from dateutil.relativedelta import relativedelta
import calendar

@login_required(login_url='login')
def add_employee(request):
    
    if request.method == 'POST':

        date_of_birth = request.POST.get("date_of_birth")
        date_of_birth = date_of_birth.split("-")
        print('----------------')
        print(date_of_birth)
        print('----------------')

        date_of_birth = datetime(int(date_of_birth[0]), int(date_of_birth[1]), int(date_of_birth[2]))
        future_date = date_of_birth + relativedelta(years=58)

        # Getting the last day of the month for the future date
        last_day = calendar.monthrange(future_date.year, future_date.month)[1]
        last_day_of_month = future_date.replace(day=last_day)
        print('----------------')

        print(last_day_of_month)
        print('----------------')

        last_day_of_month.strftime("%Y-%m-%d")
        updated_request = request.POST.copy()
        updated_request.update({'date_of_retirement': last_day_of_month})


        forms = employee_Form(updated_request)

        if forms.is_valid():
            forms.save()
            return redirect('list_employee')
        else:
            print(forms.errors)
            return redirect('list_employee')
    
    else:

        forms = employee_Form()
      
        employee_data = employee.objects.all()

        
        context = {
            'form': forms,
            'employee_data': employee_data,
        }

        return render(request, 'store/add_employee.html', context)

@login_required(login_url='login')
def update_employee(request, employee_id):

    if request.method == 'POST':

        instance = employee.objects.get(id=employee_id)

        forms = employee_Form(request.POST, instance = instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_employee')
    
    else:

        instance = employee.objects.get(id=employee_id)

        

        forms = employee_Form(instance = instance)

        context = {
            'form': forms,
        }

        return render(request, 'store/add_employee.html', context)


@login_required(login_url='login')
def delete_employee(request, employee_id):
    
    employee.objects.get(id=employee_id).delete()

    return HttpResponseRedirect(reverse('list_employee_delete'))


@login_required(login_url='login')
def list_employee(request):
    
     
    data = employee.objects.all().order_by('name')

    context = {
            'data': data
        }


    return render(request, 'store/list_employee.html', context)

import json

@login_required(login_url='login')
def retiredmentdate(request):
    
     
    date_of_birth = request.POST.get("date_of_birth")
    date_of_birth = date_of_birth.split("-")
    print('----------------')
    print(date_of_birth)
    print('----------------')

    date_of_birth = datetime(int(date_of_birth[0]), int(date_of_birth[1]), int(date_of_birth[2]))
    future_date = date_of_birth + relativedelta(years=58)

    # Getting the last day of the month for the future date
    last_day = calendar.monthrange(future_date.year, future_date.month)[1]
    last_day_of_month = future_date.replace(day=last_day)
    print('----------------')

    print(last_day_of_month)
    print('----------------')

    last_day_of_month = last_day_of_month.strftime("%Y-%m-%d")


    
    some_data_to_dump = {
        'date': last_day_of_month,
    }


    return JsonResponse(some_data_to_dump) 







@login_required(login_url='login')
def add_emp_classes(request):
    
    if request.method == 'POST':

        forms = emp_classes_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_emp_classes')
        else:
            print(forms.errors)
            return redirect('list_emp_classes')
    
    else:

        forms = emp_classes_Form()
      
        emp_classes_data = emp_classes.objects.all()

        
        context = {
            'form': forms,
            'emp_classes_data': emp_classes_data,
        }

        return render(request, 'store/add_emp_classes.html', context)

@login_required(login_url='login')
def update_emp_classes(request, emp_classes_id):

    if request.method == 'POST':

        instance = emp_classes.objects.get(id=emp_classes_id)

        forms = emp_classes_Form(request.POST, instance = instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_emp_classes')
    
    else:

        instance = emp_classes.objects.get(id=emp_classes_id)

        

        forms = emp_classes_Form(instance = instance)

        context = {
            'form': forms,
        }

        return render(request, 'store/add_emp_classes.html', context)


@login_required(login_url='login')
def delete_emp_classes(request, emp_classes_id):
    
    emp_classes.objects.get(id=emp_classes_id).delete()

    return HttpResponseRedirect(reverse('list_emp_classes_delete'))


@login_required(login_url='login')
def list_emp_classes(request):
    
     
    data = emp_classes.objects.all().order_by('name')

    context = {
            'data': data
        }


    return render(request, 'store/list_emp_classes.html', context)





@login_required(login_url='login')
def add_allowance(request):
    
    if request.method == 'POST':

        forms = allowance_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_allowance')
        else:
            print(forms.errors)
            return redirect('list_allowance')
    
    else:

        forms = allowance_Form()
      
        allowance_data = allowance.objects.all()

        
        context = {
            'form': forms,
            'allowance_data': allowance_data,
        }

        return render(request, 'store/add_allowance.html', context)

@login_required(login_url='login')
def update_allowance(request, allowance_id):

    if request.method == 'POST':

        instance = allowance.objects.get(id=allowance_id)

        forms = allowance_Form(request.POST, instance = instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_allowance')
    
    else:

        instance = allowance.objects.get(id=allowance_id)

        

        forms = allowance_Form(instance = instance)

        context = {
            'form': forms,
        }

        return render(request, 'store/add_allowance.html', context)


@login_required(login_url='login')
def delete_allowance(request, allowance_id):
    
    allowance.objects.get(id=allowance_id).delete()

    return HttpResponseRedirect(reverse('list_allowance_delete'))


@login_required(login_url='login')
def list_allowance(request):
    
     
    data = allowance.objects.all().order_by('name')

    context = {
            'data': data
        }


    return render(request, 'store/list_allowance.html', context)



@login_required(login_url='login')
def add_deduction(request):
    
    if request.method == 'POST':

        forms = deduction_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_deduction')
        else:
            print(forms.errors)
            return redirect('list_deduction')
    
    else:

        forms = deduction_Form()
      
        deduction_data = deduction.objects.all()

        
        context = {
            'form': forms,
            'deduction_data': deduction_data,
        }

        return render(request, 'store/add_deduction.html', context)

@login_required(login_url='login')
def update_deduction(request, deduction_id):

    if request.method == 'POST':

        instance = deduction.objects.get(id=deduction_id)

        forms = deduction_Form(request.POST, instance = instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_deduction')
    
    else:

        instance = deduction.objects.get(id=deduction_id)

        

        forms = deduction_Form(instance = instance)

        context = {
            'form': forms,
        }

        return render(request, 'store/add_deduction.html', context)


@login_required(login_url='login')
def delete_deduction(request, deduction_id):
    
    deduction.objects.get(id=deduction_id).delete()

    return HttpResponseRedirect(reverse('list_deduction_delete'))


@login_required(login_url='login')
def list_deduction(request):
    
     
    data = deduction.objects.all().order_by('name')

    context = {
            'data': data
        }


    return render(request, 'store/list_deduction.html', context)


@login_required(login_url='login')
def add_miscellaneous_deduction(request):
    
    if request.method == 'POST':

        forms = miscellaneous_deduction_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_miscellaneous_deduction')
        else:
            print(forms.errors)
            return redirect('list_miscellaneous_deduction')
    
    else:

        forms = miscellaneous_deduction_Form()
      
        miscellaneous_deduction_data = miscellaneous_deduction.objects.all()

        
        context = {
            'form': forms,
            'miscellaneous_deduction_data': miscellaneous_deduction_data,
        }

        return render(request, 'store/add_miscellaneous_deduction.html', context)

@login_required(login_url='login')
def update_miscellaneous_deduction(request, miscellaneous_deduction_id):

    if request.method == 'POST':

        instance = miscellaneous_deduction.objects.get(id=miscellaneous_deduction_id)

        forms = miscellaneous_deduction_Form(request.POST, instance = instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_miscellaneous_deduction')
    
    else:

        instance = miscellaneous_deduction.objects.get(id=miscellaneous_deduction_id)

        

        forms = miscellaneous_deduction_Form(instance = instance)

        context = {
            'form': forms,
        }

        return render(request, 'store/add_miscellaneous_deduction.html', context)


@login_required(login_url='login')
def delete_miscellaneous_deduction(request, miscellaneous_deduction_id):
    
    miscellaneous_deduction.objects.get(id=miscellaneous_deduction_id).delete()

    return HttpResponseRedirect(reverse('list_miscellaneous_deduction_delete'))


@login_required(login_url='login')
def list_miscellaneous_deduction(request):
    
     
    data = miscellaneous_deduction.objects.all().order_by('name')

    context = {
            'data': data
        }


    return render(request, 'store/list_miscellaneous_deduction.html', context)





@login_required(login_url='login')
def add_emp_classes(request):
    
    if request.method == 'POST':

        forms = emp_classes_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_emp_classes')
        else:
            print(forms.errors)
            return redirect('list_emp_classes')
    
    else:

        forms = emp_classes_Form()
      
        emp_classes_data = emp_classes.objects.all()

        
        context = {
            'form': forms,
            'emp_classes_data': emp_classes_data,
        }

        return render(request, 'store/add_emp_classes.html', context)

@login_required(login_url='login')
def update_emp_classes(request, emp_classes_id):

    if request.method == 'POST':

        instance = emp_classes.objects.get(id=emp_classes_id)

        forms = emp_classes_Form(request.POST, instance = instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_emp_classes')
    
    else:

        instance = emp_classes.objects.get(id=emp_classes_id)

        

        forms = emp_classes_Form(instance = instance)

        context = {
            'form': forms,
        }

        return render(request, 'store/add_emp_classes.html', context)


@login_required(login_url='login')
def delete_emp_classes(request, emp_classes_id):
    
    emp_classes.objects.get(id=emp_classes_id).delete()

    return HttpResponseRedirect(reverse('list_emp_classes_delete'))


@login_required(login_url='login')
def list_emp_classes(request):
    
     
    data = emp_classes.objects.all().order_by('name')

    context = {
            'data': data
        }


    return render(request, 'store/list_emp_classes.html', context)


@login_required(login_url='login')
def add_loan(request):
    
    if request.method == 'POST':

        forms = loan_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_loan')
        else:
            print(forms.errors)
            return redirect('list_loan')
    
    else:

        forms = loan_Form()
      
        loan_data = loan.objects.all()

        
        context = {
            'form': forms,
            'loan_data': loan_data,
        }

        return render(request, 'store/add_loan.html', context)

@login_required(login_url='login')
def update_loan(request, loan_id):

    if request.method == 'POST':

        instance = loan.objects.get(id=loan_id)

        forms = loan_Form(request.POST, instance = instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_loan')
    
    else:

        instance = loan.objects.get(id=loan_id)

        

        forms = loan_Form(instance = instance)

        context = {
            'form': forms,
        }

        return render(request, 'store/add_loan.html', context)


@login_required(login_url='login')
def delete_loan(request, loan_id):
    
    loan.objects.get(id=loan_id).delete()

    return HttpResponseRedirect(reverse('list_loan_delete'))


@login_required(login_url='login')
def list_loan(request):
    
     
    data = loan.objects.all().order_by('name')

    context = {
            'data': data
        }


    return render(request, 'store/list_loan.html', context)




@login_required(login_url='login')
def add_bank(request):
    
    if request.method == 'POST':

        forms = bank_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_bank')
        else:
            print(forms.errors)
            return redirect('list_bank')
    
    else:

        forms = bank_Form()
      
        bank_data = bank.objects.all()

        
        context = {
            'form': forms,
            'bank_data': bank_data,
        }

        return render(request, 'store/add_bank.html', context)

@login_required(login_url='login')
def update_bank(request, bank_id):

    if request.method == 'POST':

        instance = bank.objects.get(id=bank_id)

        forms = bank_Form(request.POST, instance = instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_bank')
    
    else:

        instance = bank.objects.get(id=bank_id)

        

        forms = bank_Form(instance = instance)

        context = {
            'form': forms,
        }

        return render(request, 'store/add_bank.html', context)


@login_required(login_url='login')
def delete_bank(request, bank_id):
    
    bank.objects.get(id=bank_id).delete()

    return HttpResponseRedirect(reverse('list_bank_delete'))


@login_required(login_url='login')
def list_bank(request):
    
     
    data = bank.objects.all().order_by('name')

    context = {
            'data': data
        }


    return render(request, 'store/list_bank.html', context)








# delete view

     

@login_required(login_url='login')
def list_company_delete(request):

    data = company.objects.all()

    context = {
        'data': data
    }

    return render(request, 'delete/list_company_delete.html', context)


@login_required(login_url='login')
def list_company_delete(request):

    data = company.objects.all()

    context = {
        'data': data
    }

    return render(request, 'delete/list_company_delete.html', context)



@login_required(login_url='login')
def list_godown_delete(request):
    
    data = godown.objects.all()
    context = {
            'data': data
        }


    return render(request, 'delete/list_godown_delete.html', context)

@login_required(login_url='login')
def list_company_goods_delete(request):
    
    data = company_goods.objects.all()
    context = {
            'data': data
        }


    return render(request, 'delete/list_company_goods_delete.html', context)



@login_required(login_url='login')
def list_goods_company_delete(request):
    
    data = goods_company.objects.all()

    context = {
            'data': data
        }


    return render(request, 'delete/list_goods_company_delete.html', context)




@login_required(login_url='login')
def list_agent_delete(request):
    
    data = agent.objects.all()

    context = {
            'data': data
        }


    return render(request, 'delete/list_agent_delete.html', context)


@login_required(login_url='login')
def list_transport_delete(request):
    
    data = transport.objects.all()

    context = {
            'data': data
        }


    return render(request, 'delete/list_transport_delete.html', context)

