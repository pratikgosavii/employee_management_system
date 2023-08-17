from email import message
from genericpath import samefile
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import pandas as pd


from store.views import numOfDays
from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from datetime import date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from functools import reduce

from django.urls import reverse
import csv
import mimetypes

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


from datetime import datetime
import pytz

IST = pytz.timezone('Asia/Kolkata')



from store.forms import *




@login_required(login_url='login')
def manage_salary(request, employee_id):

    employee_instance = employee.objects.get(id = employee_id)


    if request.method == 'POST':

        forms = employee_Form(request.POST, instance = employee_instance)

        if forms.is_valid():

            forms.save()

            return redirect('list_employee')


        else:
            print(forms.errors)
            allowance_data = employee_allowance.objects.filter(employee = employee_instance)
            deduction_data = employee_deduction.objects.filter(employee = employee_instance)
            loan_data = employee_loan.objects.filter(employee = employee_instance)
            miscellaneous_deduction_data = employee_miscellaneous_deduction.objects.filter(employee = employee_instance)

            form_allowance = allowance_Form()
            form_employee_allowance = employee_allowance_Form()
            form_employee_deduction = employee_deduction_Form()
            form_employee_loan = employee_loan_Form()
            form_employee_miscellaneous_deduction = employee_miscellaneous_deduction_Form()

        
            context = {
                'form': forms,
                'employee_id' : employee_id,
                'allowance_data': allowance_data,
                'deduction_data': deduction_data,
                'loan_data': loan_data,
                'miscellaneous_deduction_data': miscellaneous_deduction_data,
                'form_allowance': form_allowance,
                'form_employee_allowance': form_employee_allowance,
                'form_employee_deduction': form_employee_deduction,
                'form_employee_loan': form_employee_loan,
                'form_employee_miscellaneous_deduction': form_employee_miscellaneous_deduction,
            }
            return render(request, 'transactions/manage_salary.html', context)


    else:

        forms = employee_Form(instance = employee_instance)


        allowance_data = employee_allowance.objects.filter(employee = employee_instance)
        deduction_data = employee_deduction.objects.filter(employee = employee_instance)
        loan_data = employee_loan.objects.filter(employee = employee_instance)
        miscellaneous_deduction_data = employee_miscellaneous_deduction.objects.filter(employee = employee_instance)

        form_allowance = allowance_Form()
        form_employee_allowance = employee_allowance_Form()
        form_employee_deduction = employee_deduction_Form()
        form_employee_loan = employee_loan_Form()
        form_employee_miscellaneous_deduction = employee_miscellaneous_deduction_Form()

       
        context = {
            'form': forms,
            'employee_id' : employee_id,
            'allowance_data': allowance_data,
            'deduction_data': deduction_data,
            'loan_data': loan_data,
            'miscellaneous_deduction_data': miscellaneous_deduction_data,
            'form_allowance': form_allowance,
            'form_employee_allowance': form_employee_allowance,
            'form_employee_deduction': form_employee_deduction,
            'form_employee_loan': form_employee_loan,
            'form_employee_miscellaneous_deduction': form_employee_miscellaneous_deduction,
        }
        return render(request, 'transactions/manage_salary.html', context)







@login_required(login_url='login')
def add_employee_allowance(request):

    employee_id = request.POST.get("employee_id")
    allowance_id = request.POST.get("allowance")

    employee_instance = employee.objects.get(id = employee_id)
    allowance_instance = allowance.objects.get(id = employee_id)


    if request.method == 'POST':

        updated_request = request.POST.copy()


        if allowance_instance.allowance.percentage:

            amount = employee_instance.basic_salary * allowance_instance.allowance.percentage / 100

        else:

            amount = allowance_instance.allowance.amount
    

        updated_request.update({'employee': employee_instance, 'amount' : amount})

        forms = employee_allowance_Form(updated_request)

        if forms.is_valid():
            forms.save()

            return redirect('manage_salary', employee_id = employee_id)
        else:
            print(forms.errors)
            return redirect('list_employee_allowance')
    
   
@login_required(login_url='login')
def update_employee_allowance(request, employee_allowance_id):

    if request.method == 'POST':

        instance = employee_allowance.objects.get(id=employee_allowance_id)

        forms = employee_allowance_Form(request.POST, instance = instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_employee_allowance')
    
    else:

        instance = employee_allowance.objects.get(id=employee_allowance_id)

        

        forms = employee_allowance_Form(instance = instance)

        context = {
            'form': forms,
        }

        return render(request, 'store/add_employee_allowance.html', context)


@login_required(login_url='login')
def delete_employee_allowance(request, employee_allowance_id):
    
    employee_instance = employee_allowance.objects.get(id=employee_allowance_id)
    employee_id = employee_instance.employee.id
    employee_instance.delete()
    return redirect('manage_salary',  employee_id=employee_id)


@login_required(login_url='login')
def list_employee_allowance(request):
    
     
    data = employee_allowance.objects.all().order_by('name')

    context = {
            'data': data
        }


    return render(request, 'store/list_employee_allowance.html', context)



@login_required(login_url='login')
def add_employee_deduction(request):

    employee_id = request.POST.get("employee_id")
    deduction_id = request.POST.get("deduction")

    employee_instance = employee.objects.get(id = employee_id)
    deduction_instance = deduction.objects.get(id = deduction_id)

    
    if request.method == 'POST':

        updated_request = request.POST.copy()
        updated_request.update({'employee': employee_instance})

        if deduction_instance.allowance.percentage:

            amount = employee_instance.basic_salary * deduction_instance.allowance.percentage / 100

        else:

            amount = deduction_instance.allowance.amount
    

        updated_request.update({'employee': employee_instance, 'amount' : amount})
        forms = employee_deduction_Form(updated_request)

        if forms.is_valid():
            forms.save()

            return redirect('manage_salary', employee_id = employee_id)
        else:
            print('------------------------')
            print('------------------------')
            print('------------------------')
            print('------------------------')
            print(forms.errors)
            return redirect('list_employee_deduction')
    
   
@login_required(login_url='login')
def update_employee_deduction(request, employee_deduction_id):

    if request.method == 'POST':

        instance = employee_deduction.objects.get(id=employee_deduction_id)

        forms = employee_deduction_Form(request.POST, instance = instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_employee_deduction')
    
    else:

        instance = employee_deduction.objects.get(id=employee_deduction_id)

        

        forms = employee_deduction_Form(instance = instance)

        context = {
            'form': forms,
        }

        return render(request, 'store/add_employee_deduction.html', context)


@login_required(login_url='login')
def delete_employee_deduction(request, employee_deduction_id):
    
    employee_instance =  employee_deduction.objects.get(id=employee_deduction_id)

    employee_id = employee_instance.employee.id
    employee_instance.delete()

    return redirect('manage_salary',  employee_id=employee_id)


@login_required(login_url='login')
def list_employee_deduction(request):
    
     
    data = employee_deduction.objects.all()

    context = {
            'data': data
        }


    return render(request, 'store/list_employee_deduction.html', context)


@login_required(login_url='login')
def add_employee_loan(request):

    employee_id = request.POST.get("employee_id")

    employee_instance = employee.objects.get(id = employee_id)

    
    if request.method == 'POST':

        updated_request = request.POST.copy()
        updated_request.update({'employee': employee_instance})

        forms = employee_loan_Form(updated_request)

        if forms.is_valid():
            forms.save()

            return redirect('manage_salary', employee_id = employee_id)
        else:
            print(forms.errors)
            return redirect('list_employee_loan')
    
   
@login_required(login_url='login')
def update_employee_loan(request, employee_loan_id):

    if request.method == 'POST':

        instance = employee_loan.objects.get(id=employee_loan_id)

        forms = employee_loan_Form(request.POST, instance = instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_employee_loan')
    
    else:

        instance = employee_loan.objects.get(id=employee_loan_id)

        

        forms = employee_loan_Form(instance = instance)

        context = {
            'form': forms,
        }

        return render(request, 'store/add_employee_loan.html', context)


@login_required(login_url='login')
def delete_employee_loan(request, employee_loan_id):
    
    employee_instance = employee_loan.objects.get(id=employee_loan_id)

    employee_id = employee_instance.employee.id
    employee_instance.delete()

    return redirect('manage_salary',  employee_id=employee_id)


@login_required(login_url='login')
def list_employee_loan(request):
    
     
    data = employee_loan.objects.all().order_by('name')

    context = {
            'data': data
        }


    return render(request, 'store/list_employee_loan.html', context)


@login_required(login_url='login')
def add_employee_miscellaneous_deduction(request):

    employee_id = request.POST.get("employee_id")

    employee_instance = employee.objects.get(id = employee_id)

    
    if request.method == 'POST':

        updated_request = request.POST.copy()
        updated_request.update({'employee': employee_instance})

        forms = employee_miscellaneous_deduction_Form(updated_request)

        if forms.is_valid():
            forms.save()

            return redirect('manage_salary', employee_id = employee_id)
        else:
            print(forms.errors)
            return redirect('list_employee_miscellaneous_deduction')
    
   
@login_required(login_url='login')
def update_employee_miscellaneous_deduction(request, employee_miscellaneous_deduction_id):

    if request.method == 'POST':

        instance = employee_miscellaneous_deduction.objects.get(id=employee_miscellaneous_deduction_id)

        forms = employee_miscellaneous_deduction_Form(request.POST, instance = instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_employee_miscellaneous_deduction')
    
    else:

        instance = employee_miscellaneous_deduction.objects.get(id=employee_miscellaneous_deduction_id)

        

        forms = employee_miscellaneous_deduction_Form(instance = instance)

        context = {
            'form': forms,
        }

        return render(request, 'store/add_employee_miscellaneous_deduction.html', context)


@login_required(login_url='login')
def delete_employee_miscellaneous_deduction(request, employee_miscellaneous_deduction_id):
    
    employee_instance = employee_miscellaneous_deduction.objects.get(id=employee_miscellaneous_deduction_id)
    
    employee_id = employee_instance.employee.id
    employee_instance.delete()


    return redirect('manage_salary',  employee_id=employee_id)


@login_required(login_url='login')
def list_employee_miscellaneous_deduction(request):
    

     
    data = employee_miscellaneous_deduction.objects.all().order_by('name')

    context = {
            'data': data
        }


    return render(request, 'store/list_employee_miscellaneous_deduction.html', context)




@login_required(login_url='login')
def add_employee_transfer_department(request):
    
    if request.method == "POST":
        
        forms = employee_department_transfer_Form(request.POST)

        if forms.is_valid():

            forms.save()

            employee_id = request.POST.get("employee")
            department_type_id = request.POST.get("new_deparment")

            employee_instance = employee.objects.get(id = int(employee_id))

            department_type_instance = department_type.objects.get(id = department_type_id)

            employee_instance.department = department_type_instance

            employee_instance.save()

            context = {
                'form' : forms
            }

            return redirect('list_employee_transfer_department')

        else:

            print(forms.errors)

            context = {
                'form' : forms
            }

            return render(request, 'transactions/add_employee_deparment_transfer.html', context)

    else:


        forms = employee_department_transfer_Form()

        context = {
            'form' : forms
        }

        return render(request, 'transactions/add_employee_deparment_transfer.html', context)

@login_required(login_url='login')
def list_employee_transfer_department(request):
    

    data = employee_department_transfer.objects.all()

    print(data) 

    context = {
        'data' : data
    }

    return render(request, 'transactions/list_transfer_department.html', context)





@login_required(login_url='login')
def add_employee_increment(request):
    
    if request.method == "POST":
        
        forms = employee_increament_Form(request.POST)

        if forms.is_valid():

            forms.save()


            new_basic = request.POST.get("new_basic")
            employee_id = request.POST.get("employee")

            print(employee_id)

            employee_id = int(employee_id)

            employee_instance = employee.objects.get(id = employee_id)

            employee_instance.basic_salary = new_basic

            employee_instance.save()
            



            context = {
                'form' : forms
            }

            return redirect('list_increment')

        else:

            print(forms.errors)

            context = {
                'form' : forms
            }

            return render(request, 'transactions/add_employee_increment.html', context)

    else:


        forms = employee_increament_Form()

        context = {
            'form' : forms
        }

        return render(request, 'transactions/add_employee_increment.html', context)

@login_required(login_url='login')
def list_increment(request):
    

    data = employee_increament.objects.all()

    print(data) 

    context = {
        'data' : data
    }

    return render(request, 'transactions/list_increment.html', context)








@login_required(login_url='login')
def post_vacancy(request):
    
    if request.method == 'POST':

        forms = vacancy_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_vacancy')
        else:
            print(forms.errors)
            return redirect('list_vacancy')
    
    else:

        forms = vacancy_Form()
      
        vacancy_data = vacancy.objects.all()

        
        context = {
            'form': forms,
            'vacancy_data': vacancy_data,
        }

        return render(request, 'transactions/post_vacancy.html', context)

@login_required(login_url='login')
def update_vacancy(request, vacancy_id):

    if request.method == 'POST':

        instance = vacancy.objects.get(id=vacancy_id)

        forms = vacancy_Form(request.POST, instance = instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_vacancy')
    
    else:

        instance = vacancy.objects.get(id=vacancy_id)

        

        forms = vacancy_Form(instance = instance)

        context = {
            'form': forms,
        }

        return render(request, 'transactions/post_vacancy.html', context)


@login_required(login_url='login')
def delete_vacancy(request, vacancy_id):
    
    vacancy.objects.get(id=vacancy_id).delete()

    return HttpResponseRedirect(reverse('list_vacancy_delete'))


@login_required(login_url='login')
def list_vacancy(request):
    
     
    data = vacancy.objects.all().order_by('name')

    context = {
            'data': data
        }


    return render(request, 'transactions/list_vacancy.html', context)


@login_required(login_url='login')
def post_leaves(request):
    
    if request.method == 'POST':

        forms = leaves_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_leaves')
        else:
            print(forms.errors)
            return redirect('list_leaves')
    
    else:

        forms = leaves_Form()
      
        leaves_data = leaves.objects.all()

        
        context = {
            'form': forms,
            'leaves_data': leaves_data,
        }

        return render(request, 'transactions/add_leaves.html', context)

@login_required(login_url='login')
def update_leaves(request, leaves_id):

    if request.method == 'POST':

        instance = leaves.objects.get(id=leaves_id)

        forms = leaves_Form(request.POST, instance = instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_leaves')
    
    else:

        instance = leaves.objects.get(id=leaves_id)

        

        forms = leaves_Form(instance = instance)

        context = {
            'form': forms,
        }

        return render(request, 'transactions/post_leaves.html', context)


@login_required(login_url='login')
def delete_leaves(request, leaves_id):
    
    leaves.objects.get(id=leaves_id).delete()

    return HttpResponseRedirect(reverse('list_leaves_delete'))


@login_required(login_url='login')
def list_leaves(request):
    
     
    data = leaves.objects.all()

    context = {
            'data': data
        }


    return render(request, 'transactions/list_leaves.html', context)


from .filters import *
import datetime
from django.db.models import Count, Sum
from django.db.models import Sum, F
from django.db.models.functions import ExtractMonth, ExtractYear
from django.db.models import Sum, Q

@login_required(login_url='login')
def list_employee_salary(request):
    
    date = request.GET.get('salary_date')

    
    if date:

        date = date.split("-")
       
        date = datetime(int(date[0]), int(date[1]), int(date[2]))

        month = date.month
        year = date.year

    else:

        current_date = datetime.now()
        month = current_date.month
        year = current_date.year

    department_type_id= request.GET.get('department')
    print('---------------------')
    print('---------------------')
    print('---------------------')
    print('---------------------')
    print(department_type_id)
    if department_type_id:

        employees = employee.objects.filter(department__id = department_type_id)

    else:

        employees = employee.objects.all()


    # Calculate total allowance and total deduction for each employee
    employee_data = []
    for emp in employees:
        total_allowance = emp.employee_allo.aggregate(total=Sum('amount'))['total']
        total_deduction = emp.employee_dedu.aggregate(total=Sum('amount'))['total']

        total_loan=emp.employee_loan_re.aggregate(total=Sum('emi'))['total'] or 0
        total_miscellaneous=emp.employee_misc.aggregate(total=Sum('miscellaneous__amount',
        filter=Q(
            date__month=month,
            date__year=year,
        ))
        )['total'] or 0
        
        employee_data.append({
            'employee': emp,
            'total_allowance': total_allowance,
            'total_deduction': total_deduction,
            'total_loan': total_loan,
            'total_miscellaneous': total_miscellaneous,
        })


    context = {
        'employee_salary_filter' : employee_salary_filter(),
        'data': employee_data,
        'month': month,
        'year': year,
        }

       
    for a in context['data']:
        print(a)
        total_allowance = a['total_allowance'] or 0
        total_deduction = a['total_deduction'] or 0
        basic_salary = a['employee'].basic_salary or 0
        total_loan = a['total_loan'] or 0
        print(total_miscellaneous)

        total_miscellaneous = a.get('total_miscellaneous', {})
        print('basic_salary')
        print(basic_salary)
        print('total_allowance')
        print(total_allowance)
        print('total_deduction')
        print(total_deduction)
        print('total_loan')
        print(total_loan)
        a['total_amount'] = basic_salary + total_allowance - total_deduction - total_loan - total_miscellaneous
        salary = employee_salary.objects.filter(employee=a['employee'], salary_date__month=month, salary_date__year=year).first()
        a['salary_done'] = bool(salary)


    print(context['data'])

    return render(request, 'transactions/employee_salary.html', context)


from django.db.models import Sum

from datetime import datetime



@login_required(login_url='login')
def generate_employee_salary(request, employee_id, month, year):
    
    date = datetime(int(year), int(month), 1)

  

    employee_instancee = employee.objects.get(id = employee_id)

    employe_basic_salary = employee_instancee.basic_salary

    allowance_amount = employee_allowance.objects.filter(employee = employee_instancee).aggregate(total_allowance=Sum('amount'))['total_allowance']
    loan_amount = employee_loan.objects.filter(employee = employee_instancee).aggregate(total_emi=Sum('emi'))['total_emi']
    miscellaneous_deduction_amount = employee_miscellaneous_deduction.objects.filter(date__month = date.month, date__year = date.year, employee = employee_instancee).aggregate(total_mis_deu=Sum('miscellaneous__amount'))['total_mis_deu']
    deduction_amount = employee_deduction.objects.filter(employee = employee_instancee).aggregate(total_dedu=Sum('amount'))['total_dedu']
    

    print('--------------')
    print('--------------')
    print('--------------')
    print('--------------')

    print(employee_instancee.name)
    print(allowance_amount)

    print('--------------')

    print('--------------')

    print('--------------')

    print('--------------')

    print('--------------')


    if allowance_amount == None:
        allowance_amount = 0
    if loan_amount == None:
        loan_amount = 0
    if miscellaneous_deduction_amount == None:
        miscellaneous_deduction_amount = 0
    if deduction_amount == None:
        deduction_amount = 0
    if employe_basic_salary == None:
        employe_basic_salary = 0

    total_salary = employe_basic_salary + allowance_amount - loan_amount - deduction_amount - miscellaneous_deduction_amount
    
    print('--------------------')
    print('--------------------')
    print('--------------------')
    print('--------------------')
    print(date)
    print('--------------------')
    print('--------------------')
    print('--------------------')
    print('--------------------')
    print('--------------------')

    
    employee_salary.objects.create(employee_id = employee_id, salary_date = date, deduction_amount = deduction_amount, allowance_amount = allowance_amount, loan_amount = loan_amount, miscellaneous_deduction_amount = miscellaneous_deduction_amount, total_salary = total_salary)

    url = reverse('employee_salary')
    url += '?' + request.GET.urlencode()

    print(url)

    return redirect(url)




@login_required(login_url='login')
def employe_salary_cutof(request, employee_id, month, year):
    
    date = datetime(int(year), int(month), 1, tzinfo=ist)

    employee_instancee = employee.objects.get(id = employee_id)
    print('---------------------')
    print(employee_instancee)
    print('---------------------')
    employe_basic_salary = employee_instancee.basic_salary

    allowance_data = employee_allowance.objects.filter(employee = employee_instancee)
    allowance_amount_sum = allowance_data.aggregate(total_allowance=Sum('amount'))['total_allowance']

    loan_data = employee_loan.objects.filter(employee = employee_instancee)
    loan_amount_sum = loan_data.aggregate(total_emi=Sum('emi'))['total_emi']

    miscellaneous_deduction_data = employee_miscellaneous_deduction.objects.filter(date = date, employee = employee_instancee)
    miscellaneous_deduction_amount_sum = miscellaneous_deduction_data.aggregate(total_mis_deu=Sum('miscellaneous__amount'))['total_mis_deu']

    deduction_data = employee_deduction.objects.filter(employee = employee_instancee)
    deduction_amount_sum = deduction_data.aggregate(total_dedu=Sum('amount'))['total_dedu']

    print('------------')
    print(deduction_data)
    print('------------')



    if not allowance_data:
        allowance_amount_sum = 0
    if not loan_data:
        loan_amount_sum = 0
    if not miscellaneous_deduction_data:
        miscellaneous_deduction_amount_sum = 0
    if not deduction_data:
        deduction_amount_sum = 0

    print(allowance_amount_sum)
    print(loan_amount_sum)
    print(miscellaneous_deduction_amount_sum)
    print(deduction_amount_sum)
    print(employe_basic_salary)

    total_salary = employe_basic_salary + allowance_amount_sum - loan_amount_sum - miscellaneous_deduction_amount_sum - deduction_amount_sum

    context = {
        'month' : month,
        'year' : year,
        'total_salary' : total_salary,
        'data' : employee_instancee,

        'allowance_data' : allowance_data,
        'loan_data' : loan_data,
        'miscellaneous_deduction_data' : miscellaneous_deduction_data,
        'deduction_data' : deduction_data,

        'allowance_amount_sum' : allowance_amount_sum,
        'loan_amount_sum' : loan_amount_sum,
        'miscellaneous_deduction_amount_sum' : miscellaneous_deduction_amount_sum,
        'deduction_amount_sum' : deduction_amount_sum,
        }


    return render(request, 'transactions/employe_salary_cutof.html', context)




@login_required(login_url='login')
def generate_employee_salary_multiple(request):

    print('------------')
    print('------------')
    print('------------')
    print('------------')
    print('------------')
    print('------------')
    print('------------')
    print('------------')
    print('------------')
    print('------------')

    year = request.POST.get('year')
    month = request.POST.get('month')
    employee_id = request.POST.getlist('employee_id[]')

    for i in employee_id:

        print(i)
    
    date = datetime(int(year), int(month), 5, tzinfo=ist)

    print('salary date')

    print(date)

    print('dadasasasasas')

    for i in employee_id:


        employee_instancee = employee.objects.get(id = i)

        employe_basic_salary = employee_instancee.basic_salary or 0

        allowance_amount = employee_allowance.objects.filter(employee = employee_instancee).aggregate(Sum('amount'))['amount__sum'] or 0
        print(allowance_amount)
        loan_amount = employee_loan.objects.filter(employee = employee_instancee).aggregate(Sum('emi'))['emi__sum'] or 0
        print(loan_amount)
        miscellaneous_deduction_amount = employee_miscellaneous_deduction.objects.filter(date = date, employee = employee_instancee).aggregate(Sum('miscellaneous__amount'))['miscellaneous__amount__sum'] or 0
        print(miscellaneous_deduction_amount)
        deduction_amount = employee_deduction.objects.filter(employee = employee_instancee).aggregate(Sum('amount'))['amount__sum'] or 0
        print(deduction_amount)

        total_salary = employe_basic_salary + allowance_amount - loan_amount - deduction_amount - miscellaneous_deduction_amount
        
        employee_salary.objects.create(employee_id = i, salary_date = date, deduction_amount = deduction_amount, allowance_amount = allowance_amount, loan_amount = loan_amount, miscellaneous_deduction_amount = miscellaneous_deduction_amount, total_salary = total_salary)

    return JsonResponse({'status' : 'done'})


from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import os
from random import randint



def render_to_file(path: str, params: dict):

    template = get_template(path)
    html = template.render(params)
    file_path = os.path.join(BASE_DIR) + 'bill.pdf'
    
    with open(file_path, 'wb') as pdf:
        pisa.pisaDocument(BytesIO(html.encode("UTF-8")), pdf)
        return file_path

@login_required(login_url='login')
def generate_employee_salary_slip(request, employee_id, month, year):
    
    date = datetime(int(year), int(month), 1, tzinfo=ist)

    employee_instancee = employee.objects.get(id = employee_id)
    print('---------------------')
    print(employee_instancee)
    print('---------------------')
    employe_basic_salary = employee_instancee.basic_salary

    allowance_data = employee_allowance.objects.filter(employee = employee_instancee)
    allowance_amount_sum = allowance_data.aggregate(total_allowance=Sum('amount'))['total_allowance']

    loan_data = employee_loan.objects.filter(employee = employee_instancee)
    loan_amount_sum = loan_data.aggregate(total_emi=Sum('emi'))['total_emi']

    miscellaneous_deduction_data = employee_miscellaneous_deduction.objects.filter(date = date, employee = employee_instancee)
    miscellaneous_deduction_amount_sum = miscellaneous_deduction_data.aggregate(total_mis_deu=Sum('miscellaneous__amount'))['total_mis_deu']

    deduction_data = employee_deduction.objects.filter(employee = employee_instancee)
    deduction_amount_sum = deduction_data.aggregate(total_dedu=Sum('amount'))['total_dedu']

    print('------------')
    print(deduction_data)
    print('------------')



    if not allowance_data:
        allowance_amount_sum = 0
    if not loan_data:
        loan_amount_sum = 0
    if not miscellaneous_deduction_data:
        miscellaneous_deduction_amount_sum = 0
    if not deduction_data:
        deduction_amount_sum = 0

    print(allowance_amount_sum)
    print(loan_amount_sum)
    print(miscellaneous_deduction_amount_sum)
    print(deduction_amount_sum)
    print(employe_basic_salary)

    total_salary = employe_basic_salary + allowance_amount_sum - loan_amount_sum - miscellaneous_deduction_amount_sum - deduction_amount_sum

    context = {
        'month' : month,
        'year' : year,
        'total_salary' : total_salary,
        'data' : employee_instancee,

        'allowance_data' : allowance_data,
        'loan_data' : loan_data,
        'miscellaneous_deduction_data' : miscellaneous_deduction_data,
        'deduction_data' : deduction_data,

        'allowance_amount_sum' : allowance_amount_sum,
        'loan_amount_sum' : loan_amount_sum,
        'miscellaneous_deduction_amount_sum' : miscellaneous_deduction_amount_sum,
        'deduction_amount_sum' : deduction_amount_sum,
        }


    return render(request, 'transactions/salary_slip.html', context)

@login_required(login_url='login')
def get_old_department_ajax(request):
    
     
    employee_id = request.POST.get('employee_id')

    employee_instance = employee.objects.get(id = employee_id)



    some_data_to_dump = {
        'value': employee_instance.department.id,
    }


    return JsonResponse((some_data_to_dump), safe = False) 



@login_required(login_url='login')
def get_old_basic_ajax(request):
    
     
    employee_id = request.POST.get('employee_id')

    employee_instance = employee.objects.get(id = employee_id)



    some_data_to_dump = {
        'value': employee_instance.basic_salary,
    }


    return JsonResponse((some_data_to_dump), safe = False) 



@login_required(login_url='login')
def monthly_salary_report(request):

    date = request.GET.get('salary_date')

    
    if date:

        date = date.split("-")
       
        date = datetime(int(date[0]), int(date[1]), int(date[2]))

        month = date.month
        year = date.year

    else:

        current_date = datetime.now()
        month = current_date.month
        year = current_date.year

    department_type_id= request.GET.get('department')
    print('---------------------')
    print('---------------------')
    print('---------------------')
    print('---------------------')
    print(department_type_id)
    if department_type_id:

        employees = employee.objects.filter(department__id = department_type_id)

    else:

        employees = employee.objects.all()


    # Calculate total allowance and total deduction for each employee
    employee_data = []
    for emp in employees:
        allowance_instance = emp.employee_allo.all()
        dearness_allowance = allowance_instance.filter(allowance__name = 'Dearness Allowance').aggregate(Sum('amount'))['amount__sum'] or 0
        house_rent_allowance = allowance_instance.filter(allowance__name = 'House Rent').aggregate(Sum('amount'))['amount__sum'] or 0
        travel_allowance = allowance_instance.filter(allowance__name = 'Travel').aggregate(Sum('amount'))['amount__sum'] or 0
        washing_clothes_allowance = allowance_instance.filter(allowance__name = 'Washing Clothes').aggregate(Sum('amount'))['amount__sum'] or 0
        
        deduction_instance = emp.employee_dedu.all()
        group_insurance = deduction_instance.filter(deduction__name = 'Group Insurance').aggregate(Sum('amount'))['amount__sum'] or 0
        bussiness_tax = deduction_instance.filter(deduction__name = 'Bussiness Tax').aggregate(Sum('amount'))['amount__sum'] or 0
        NPS_employee_contribution = deduction_instance.filter(deduction__name = 'NPS Employee Contribution 10%').aggregate(Sum('amount'))['amount__sum'] or 0
        GPF_deduction = deduction_instance.filter(deduction__name = 'GPF').aggregate(Sum('amount'))['amount__sum'] or 0
        GPF_loan_deduction = deduction_instance.filter(deduction__name = 'GPF Loan').aggregate(Sum('amount'))['amount__sum'] or 0
        life_insurance = deduction_instance.filter(deduction__name = 'Life Insurance').aggregate(Sum('amount'))['amount__sum'] or 0
        accidental_insurance = deduction_instance.filter(deduction__name = 'Accidental Insurance').aggregate(Sum('amount'))['amount__sum'] or 0
        np_employee_credit_union_deduction = deduction_instance.filter(deduction__name = 'N. P Employee Credit Union Deduction').aggregate(Sum('amount'))['amount__sum'] or 0

        total_allowance = allowance_instance.aggregate(total=Sum('amount'))['total'] or 0
        total_deduction = emp.employee_dedu.aggregate(total=Sum('amount'))['total'] or 0
 
        total_loan=emp.employee_loan_re.aggregate(total=Sum('emi'))['total'] or 0
        total_miscellaneous=emp.employee_misc.aggregate(total=Sum('miscellaneous__amount',
        filter=Q(
            date__month=month,
            date__year=year,
        ))
        )['total'] or 0

        increment = employee_increament.objects.filter(employee=emp,incerement_date__lte=datetime(year, month, 1)).order_by('-incerement_date').first()

        if increment:
            basic_salary = increment.new_basic
        else:
            basic_salary = emp.basic_salary
            
        total_amount = basic_salary + total_allowance - total_deduction - total_loan - total_miscellaneous

        salary = employee_salary.objects.filter(employee=emp, salary_date__month=month, salary_date__year=year).first()
        a = bool(salary)
        if a:


            
            employee_data.append({
                'employee': emp,
                'total_allowance': total_allowance,
                'dearness_allowance': dearness_allowance,
                'house_rent_allowance': house_rent_allowance,
                'travel_allowance': travel_allowance,
                'washing_clothes_allowance': washing_clothes_allowance,
                'group_insurance': group_insurance,
                'bussiness_tax': bussiness_tax,
                'NPS_employee_contribution': NPS_employee_contribution,
                'GPF_deduction': GPF_deduction,
                'GPF_loan_deduction': GPF_loan_deduction,
                'life_insurance': life_insurance,
                'accidental_insurance': accidental_insurance,
                'np_employee_credit_union_deduction': np_employee_credit_union_deduction,
                'travel_allowance': travel_allowance,
                'total_deduction': total_deduction,
                'total_loan': total_loan,
                'total_miscellaneous': total_miscellaneous,
                'total_amount': total_amount,
            })


    context = {
        'employee_salary_filter' : employee_salary_filter(),
        'data': employee_data,
        'month': month,
        'year': year,
        }



    print(context['data'])


    return render(request, 'report/monthly_salary_report.html', context)



def download_monthly_salary_report_csv(request):


    date = request.GET.get('salary_date')

    
    if date:

        date = date.split("-")
       
        date = datetime(int(date[0]), int(date[1]), int(date[2]))

        month = date.month
        year = date.year

    else:

        current_date = datetime.now()
        month = current_date.month
        year = current_date.year

    department_type_id= request.GET.get('department')
    print('---------------------')
    print('---------------------')
    print('---------------------')
    print('---------------------')
    print(department_type_id)
    if department_type_id:

        employees = employee.objects.filter(department__id = department_type_id)

    else:

        employees = employee.objects.all()


    # Calculate total allowance and total deduction for each employee
    csv_data = []
    employee_data = []


    employee_data.append('Name')
    employee_data.append('Department')
    employee_data.append('Designation')
    employee_data.append('Working days')
    employee_data.append('Absent days')
    employee_data.append('Basic Salary')
    employee_data.append('Dearness Allowance')
    employee_data.append('House Rent')
    employee_data.append('Travel')
    employee_data.append('Washing Clothes')
    employee_data.append('Total Allowances')
    employee_data.append('Group Insurance')
    employee_data.append('Bussiness Tax')
    employee_data.append('NPS Employee Contribution 10%')
    employee_data.append('GPF')
    employee_data.append('GPF Loan')
    employee_data.append('Life Insurance')
    employee_data.append('Accidental Insurance')
    employee_data.append('N. P Employee Credit Union Deduction')
    employee_data.append('Total Deduction')
    employee_data.append('In Hand')
    csv_data.append(employee_data)
    employee_data = []

    for emp in employees:
        allowance_instance = emp.employee_allo.all()
        dearness_allowance = allowance_instance.filter(allowance__name = 'Dearness Allowance').aggregate(Sum('amount'))['amount__sum'] or 0
        house_rent_allowance = allowance_instance.filter(allowance__name = 'House Rent').aggregate(Sum('amount'))['amount__sum'] or 0
        travel_allowance = allowance_instance.filter(allowance__name = 'Travel').aggregate(Sum('amount'))['amount__sum'] or 0
        washing_clothes_allowance = allowance_instance.filter(allowance__name = 'Washing Clothes').aggregate(Sum('amount'))['amount__sum'] or 0
       
        deduction_instance = emp.employee_dedu.all()
        group_insurance = deduction_instance.filter(deduction__name = 'Group Insurance').aggregate(Sum('amount'))['amount__sum'] or 0
        bussiness_tax = deduction_instance.filter(deduction__name = 'Bussiness Tax').aggregate(Sum('amount'))['amount__sum'] or 0
        NPS_employee_contribution = deduction_instance.filter(deduction__name = 'NPS Employee Contribution').aggregate(Sum('amount'))['amount__sum'] or 0
        GPF_deduction = deduction_instance.filter(deduction__name = 'GPF').aggregate(Sum('amount'))['amount__sum'] or 0
        GPF_loan_deduction = deduction_instance.filter(deduction__name = 'GPF Loan').aggregate(Sum('amount'))['amount__sum'] or 0
        life_insurance = deduction_instance.filter(deduction__name = 'Life Insurance').aggregate(Sum('amount'))['amount__sum'] or 0
        accidental_insurance = deduction_instance.filter(deduction__name = 'Accidental Insurance').aggregate(Sum('amount'))['amount__sum'] or 0
        np_employee_credit_union_deduction = deduction_instance.filter(deduction__name = 'N. P Employee Credit Union Deduction').aggregate(Sum('amount'))['amount__sum'] or 0

        total_allowance = allowance_instance.aggregate(total=Sum('amount'))['total'] or 0
        total_deduction = emp.employee_dedu.aggregate(total=Sum('amount'))['total'] or 0
 
        total_loan=emp.employee_loan_re.aggregate(total=Sum('emi'))['total'] or 0
        total_miscellaneous=emp.employee_misc.aggregate(total=Sum('miscellaneous__amount',
        filter=Q(
            date__month=month,
            date__year=year,
        ))
        )['total'] or 0


        

        in_hand= emp.basic_salary + total_allowance - total_deduction - total_loan - total_miscellaneous
        salary = employee_salary.objects.filter(employee=emp, salary_date__month=month, salary_date__year=year).first()
        a = bool(salary)

        if a:
            
            employee_data.append(str(emp.name) + ' ' + str(emp.middle_name) + ' ' + str(emp.last_name))
            employee_data.append(emp.department)
            employee_data.append(emp.designation)
            employee_data.append(20)
            employee_data.append(30)
            employee_data.append(emp.basic_salary)
            employee_data.append(dearness_allowance)
            employee_data.append(house_rent_allowance)
            employee_data.append(travel_allowance)
            employee_data.append(washing_clothes_allowance)
            employee_data.append(total_allowance)
            employee_data.append(group_insurance)
            employee_data.append(bussiness_tax)
            employee_data.append(NPS_employee_contribution)
            employee_data.append(GPF_deduction)
            employee_data.append(GPF_loan_deduction)
            employee_data.append(life_insurance)
            employee_data.append(accidental_insurance)
            employee_data.append(np_employee_credit_union_deduction)
            employee_data.append(total_deduction)
            employee_data.append(in_hand)
            csv_data.append(employee_data)
            employee_data = []
       
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    csv_writer = csv.writer(response)
    for row in csv_data:
        csv_writer.writerow(row)

    return response

@login_required(login_url='login')
def bank_report(request):

    date = request.GET.get('salary_date')

    
    if date:

        date = date.split("-")
       
        date = datetime(int(date[0]), int(date[1]), int(date[2]))

        month = date.month
        year = date.year

    else:

        current_date = datetime.now()
        month = current_date.month
        year = current_date.year

    department_type_id= request.GET.get('department')
    print('---------------------')
    print('---------------------')
    print('---------------------')
    print('---------------------')
    print(department_type_id)
    if department_type_id:

        employees = employee.objects.filter(department__id = department_type_id)

    else:

        employees = employee.objects.all()


    # Calculate total allowance and total deduction for each employee
    employee_data = []
    for emp in employees:
       
        total_allowance = emp.employee_allo.aggregate(total=Sum('amount'))['total'] or 0
        total_deduction = emp.employee_dedu.aggregate(total=Sum('amount'))['total'] or 0
 
        total_loan=emp.employee_loan_re.aggregate(total=Sum('emi'))['total'] or 0
        total_miscellaneous=emp.employee_misc.aggregate(total=Sum('miscellaneous__amount',
        filter=Q(
            date__month=month,
            date__year=year,
        ))
        )['total'] or 0


        
        total_amount = emp.basic_salary + total_allowance - total_deduction - total_loan - total_miscellaneous
        salary = employee_salary.objects.filter(employee=emp, salary_date__month=month, salary_date__year=year).first()
        a = bool(salary)
        if a:

            employee_data.append({
                'employee': emp,
                'total_amount': total_amount,
            })


    context = {
        'employee_salary_filter' : employee_salary_filter(),
        'data': employee_data,
        'month': month,
        'year': year,
        }




    return render(request, 'report/bank_report.html', context)



def download_bank_report_csv(request):


    date = request.GET.get('salary_date')

    
    if date:

        date = date.split("-")
       
        date = datetime(int(date[0]), int(date[1]), int(date[2]))

        month = date.month
        year = date.year

    else:

        current_date = datetime.now()
        month = current_date.month
        year = current_date.year

    department_type_id= request.GET.get('department')
    print('---------------------')
    print('---------------------')
    print('---------------------')
    print('---------------------')
    print(department_type_id)
    if department_type_id:

        employees = employee.objects.filter(department__id = department_type_id)

    else:

        employees = employee.objects.all()


    # Calculate total allowance and total deduction for each employee
    csv_data = []
    employee_data = []


    employee_data.append('Name')
    employee_data.append('Department')
    employee_data.append('Bank Account')
    employee_data.append('In Hand')
    csv_data.append(employee_data)
    employee_data = []

    for emp in employees:
        total_allowance = emp.employee_allo.aggregate(total=Sum('amount'))['total'] or 0
        total_deduction = emp.employee_dedu.aggregate(total=Sum('amount'))['total'] or 0
 
        total_loan=emp.employee_loan_re.aggregate(total=Sum('emi'))['total'] or 0
        total_miscellaneous=emp.employee_misc.aggregate(total=Sum('miscellaneous__amount',
        filter=Q(
            date__month=month,
            date__year=year,
        ))
        )['total'] or 0


        increment = employee_increament.objects.filter(employee=emp,incerement_date__lte=datetime(year, month, 1)).order_by('-incerement_date').first()

        if increment:
            basic_salary = increment.new_basic
        else:
            basic_salary = emp.basic_salary
            
        total_amount = basic_salary + total_allowance - total_deduction - total_loan - total_miscellaneous
        
        salary = employee_salary.objects.filter(employee=emp, salary_date__month=month, salary_date__year=year).first()
        a = bool(salary)
        if a:

            employee_data.append(str(emp.name) + ' ' + str(emp.middle_name) + ' ' + str(emp.last_name))
            employee_data.append(emp.department)
            employee_data.append(emp.bank_ac_no)
            employee_data.append(total_amount)
            csv_data.append(employee_data)
            employee_data = []
       
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    csv_writer = csv.writer(response)
    for row in csv_data:
        csv_writer.writerow(row)

    return response

@login_required(login_url='login')
def dcps_report(request):

    date = request.GET.get('salary_date')

    
    if date:

        date = date.split("-")
       
        date = datetime(int(date[0]), int(date[1]), int(date[2]))

        month = date.month
        year = date.year

    else:

        current_date = datetime.now()
        month = current_date.month
        year = current_date.year

    department_type_id= request.GET.get('department')
    print('---------------------')
    print('---------------------')
    print('---------------------')
    print('---------------------')
    print(department_type_id)
    if department_type_id:

        print('----------fdfdfdfdf-----------')
        print('---------------------')
        total_dcps = employee.objects.filter(department__id = department_type_id, employee_salary__salary_date__month=month, employee_salary__salary_date__year=year).annotate(total_dcp=Sum('dcps'))

    else:

            
        print('---------------------')
        print('---------------------')

        total_dcps = employee.objects.filter(employee_salary__salary_date__month=month, employee_salary__salary_date__year=year).annotate(total_dcp=Sum('dcps'))



    print('---------------------')
    print('---------------------')

    # Calculate total allowance and total deduction for each employee
       



       

    context = {
        'employee_salary_filter' : employee_salary_filter(),
        'data': total_dcps,
        'month': month,
        'year': year,
        }




    return render(request, 'report/dcps_report.html', context)



def download_dcps_report_csv(request):


    date = request.GET.get('salary_date')

    
    if date:

        date = date.split("-")
       
        date = datetime(int(date[0]), int(date[1]), int(date[2]))

        month = date.month
        year = date.year

    else:

        current_date = datetime.now()
        month = current_date.month
        year = current_date.year

    department_type_id= request.GET.get('department')
    print('---------------------')
    print('---------------------')
    print('---------------------')
    print('---------------------')
    print(department_type_id)
    if department_type_id:

        total_dcps = employee.objects.filter(department__id = department_type_id, employee_salary__salary_date__month=month, employee_salary__salary_date__year=year).aggregate(total=Sum('dcps'))['total'] or 0

    else:

        total_dcps = employee.objects.filter(employee_salary__salary_date__month=month, employee_salary__salary_date__year=year).aggregate(total=Sum('dcps'))['total'] or 0


    # Calculate total allowance and total deduction for each employee
    csv_data = []
    employee_data = []


    employee_data.append('Name')
    employee_data.append('Department')
    employee_data.append('DCPS Account')
    csv_data.append(employee_data)
    employee_data = []

    for emp in total_dcps:

        employee_data.append(str(emp.name) + ' ' + str(emp.middle_name) + ' ' + str(emp.last_name))
        employee_data.append(emp.department)
        employee_data.append(emp.total_dcps)
        csv_data.append(employee_data)
        employee_data = []
       
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    csv_writer = csv.writer(response)
    for row in csv_data:
        csv_writer.writerow(row)

    return response

@login_required(login_url='login')
def dept_wise_report(request):

   
    date = request.GET.get('salary_date')

    
    if date:

        date = date.split("-")
       
        date = datetime(int(date[0]), int(date[1]), int(date[2]))

        month = date.month
        year = date.year

    else:

        current_date = datetime.now()
        month = current_date.month
        year = current_date.year

    department_type_id= request.GET.get('department')
    print('---------------------')
    print('------department---------------')
    print('---------------------')
    print('---------------------')
    print(department_type_id)
    if department_type_id:

        employees = employee.objects.filter(department__id__in = department_type_id)

    else:

        employees = employee.objects.all()


    # Calculate total allowance and total deduction for each employee
    employee_data = []
    for emp in employees:
        allowance_instance = emp.employee_allo.all()
        dearness_allowance = allowance_instance.filter(allowance__name = 'Dearness Allowance').aggregate(Sum('amount'))['amount__sum'] or 0
        house_rent_allowance = allowance_instance.filter(allowance__name = 'House Rent').aggregate(Sum('amount'))['amount__sum'] or 0
        travel_allowance = allowance_instance.filter(allowance__name = 'Travel').aggregate(Sum('amount'))['amount__sum'] or 0
        washing_clothes_allowance = allowance_instance.filter(allowance__name = 'Washing Clothes').aggregate(Sum('amount'))['amount__sum'] or 0
        
        deduction_instance = emp.employee_dedu.all()
        group_insurance = deduction_instance.filter(deduction__name = 'Group Insurance').aggregate(Sum('amount'))['amount__sum'] or 0
        bussiness_tax = deduction_instance.filter(deduction__name = 'Bussiness Tax').aggregate(Sum('amount'))['amount__sum'] or 0
        NPS_employee_contribution = deduction_instance.filter(deduction__name = 'NPS Employee Contribution 10%').aggregate(Sum('amount'))['amount__sum'] or 0
        GPF_deduction = deduction_instance.filter(deduction__name = 'GPF').aggregate(Sum('amount'))['amount__sum'] or 0
        GPF_loan_deduction = deduction_instance.filter(deduction__name = 'GPF Loan').aggregate(Sum('amount'))['amount__sum'] or 0
        life_insurance = deduction_instance.filter(deduction__name = 'Life Insurance').aggregate(Sum('amount'))['amount__sum'] or 0
        accidental_insurance = deduction_instance.filter(deduction__name = 'Accidental Insurance').aggregate(Sum('amount'))['amount__sum'] or 0
        np_employee_credit_union_deduction = deduction_instance.filter(deduction__name = 'N. P Employee Credit Union Deduction').aggregate(Sum('amount'))['amount__sum'] or 0

        total_allowance = allowance_instance.aggregate(total=Sum('amount'))['total'] or 0
        total_deduction = emp.employee_dedu.aggregate(total=Sum('amount'))['total'] or 0
 
        total_loan=emp.employee_loan_re.aggregate(total=Sum('emi'))['total'] or 0
        total_miscellaneous=emp.employee_misc.aggregate(total=Sum('miscellaneous__amount',
        filter=Q(
            date__month=month,
            date__year=year,
        ))
        )['total'] or 0

        increment = employee_increament.objects.filter(employee=emp,incerement_date__lte=datetime(year, month, 1)).order_by('-incerement_date').first()

        if increment:
            basic_salary = increment.new_basic
        else:
            basic_salary = emp.basic_salary

        increment = employee_increament.objects.filter(employee=emp,incerement_date__lte=datetime(year, month, 1)).order_by('-incerement_date').first()

        if increment:
            basic_salary = increment.new_basic
        else:
            basic_salary = emp.basic_salary
            
        total_amount = basic_salary + total_allowance - total_deduction - total_loan - total_miscellaneous

        salary = employee_salary.objects.filter(employee=emp, salary_date__month=month, salary_date__year=year).first()
        a = bool(salary)
        if a:


            
            employee_data.append({
                'employee': emp,
                'total_allowance': total_allowance,
                'dearness_allowance': dearness_allowance,
                'house_rent_allowance': house_rent_allowance,
                'travel_allowance': travel_allowance,
                'washing_clothes_allowance': washing_clothes_allowance,
                'group_insurance': group_insurance,
                'bussiness_tax': bussiness_tax,
                'NPS_employee_contribution': NPS_employee_contribution,
                'GPF_deduction': GPF_deduction,
                'GPF_loan_deduction': GPF_loan_deduction,
                'life_insurance': life_insurance,
                'accidental_insurance': accidental_insurance,
                'np_employee_credit_union_deduction': np_employee_credit_union_deduction,
                'travel_allowance': travel_allowance,
                'total_deduction': total_deduction,
                'total_loan': total_loan,
                'total_miscellaneous': total_miscellaneous,
                'total_amount': total_amount,
            })


    context = {
        'employee_salary_filter' : employee_salary_filter(),
        'data': employee_data,
        'month': month,
        'form': employee_Form(),
        'year': year,
        }





    return render(request, 'report/dept_wise_report.html', context)



def download_dcps_report_csv(request):


    date = request.GET.get('salary_date')

    
    if date:

        date = date.split("-")
       
        date = datetime(int(date[0]), int(date[1]), int(date[2]))

        month = date.month
        year = date.year

    else:

        current_date = datetime.now()
        month = current_date.month
        year = current_date.year

    department_type_id= request.GET.get('department')
    print('---------------------')
    print('---------------------')
    print('---------------------')
    print('---------------------')
    print(department_type_id)
    if department_type_id:

        employees = employee.objects.filter(department__id__in = department_type_id)

    else:

        employees = employee.objects.all()


    # Calculate total allowance and total deduction for each employee
    csv_data = []
    employee_data = []


    employee_data.append('Name')
    employee_data.append('Department')
    employee_data.append('Designation')
    employee_data.append('Working days')
    employee_data.append('Absent days')
    employee_data.append('Basic Salary')
    employee_data.append('Dearness Allowance')
    employee_data.append('House Rent')
    employee_data.append('Travel')
    employee_data.append('Washing Clothes')
    employee_data.append('Total Allowances')
    employee_data.append('Group Insurance')
    employee_data.append('Bussiness Tax')
    employee_data.append('NPS Employee Contribution 10%')
    employee_data.append('GPF')
    employee_data.append('GPF Loan')
    employee_data.append('Life Insurance')
    employee_data.append('Accidental Insurance')
    employee_data.append('N. P Employee Credit Union Deduction')
    employee_data.append('Total Deduction')
    employee_data.append('In Hand')
    csv_data.append(employee_data)
    employee_data = []

    for emp in employees:
        allowance_instance = emp.employee_allo.all()
        dearness_allowance = allowance_instance.filter(allowance__name = 'Dearness Allowance').aggregate(Sum('amount'))['amount__sum'] or 0
        house_rent_allowance = allowance_instance.filter(allowance__name = 'House Rent').aggregate(Sum('amount'))['amount__sum'] or 0
        travel_allowance = allowance_instance.filter(allowance__name = 'Travel').aggregate(Sum('amount'))['amount__sum'] or 0
        washing_clothes_allowance = allowance_instance.filter(allowance__name = 'Washing Clothes').aggregate(Sum('amount'))['amount__sum'] or 0
       
        deduction_instance = emp.employee_dedu.all()
        group_insurance = deduction_instance.filter(deduction__name = 'Group Insurance').aggregate(Sum('amount'))['amount__sum'] or 0
        bussiness_tax = deduction_instance.filter(deduction__name = 'Bussiness Tax').aggregate(Sum('amount'))['amount__sum'] or 0
        NPS_employee_contribution = deduction_instance.filter(deduction__name = 'NPS Employee Contribution').aggregate(Sum('amount'))['amount__sum'] or 0
        GPF_deduction = deduction_instance.filter(deduction__name = 'GPF').aggregate(Sum('amount'))['amount__sum'] or 0
        GPF_loan_deduction = deduction_instance.filter(deduction__name = 'GPF Loan').aggregate(Sum('amount'))['amount__sum'] or 0
        life_insurance = deduction_instance.filter(deduction__name = 'Life Insurance').aggregate(Sum('amount'))['amount__sum'] or 0
        accidental_insurance = deduction_instance.filter(deduction__name = 'Accidental Insurance').aggregate(Sum('amount'))['amount__sum'] or 0
        np_employee_credit_union_deduction = deduction_instance.filter(deduction__name = 'N. P Employee Credit Union Deduction').aggregate(Sum('amount'))['amount__sum'] or 0

        total_allowance = allowance_instance.aggregate(total=Sum('amount'))['total'] or 0
        total_deduction = emp.employee_dedu.aggregate(total=Sum('amount'))['total'] or 0
 
        total_loan=emp.employee_loan_re.aggregate(total=Sum('emi'))['total'] or 0
        total_miscellaneous=emp.employee_misc.aggregate(total=Sum('miscellaneous__amount',
        filter=Q(
            date__month=month,
            date__year=year,
        ))
        )['total'] or 0


        

        in_hand= emp.basic_salary + total_allowance - total_deduction - total_loan - total_miscellaneous
        salary = employee_salary.objects.filter(employee=emp, salary_date__month=month, salary_date__year=year).first()
        a = bool(salary)

        if a:
            
            employee_data.append(str(emp.name) + ' ' + str(emp.middle_name) + ' ' + str(emp.last_name))
            employee_data.append(emp.department)
            employee_data.append(emp.designation)
            employee_data.append(20)
            employee_data.append(30)
            employee_data.append(emp.basic_salary)
            employee_data.append(dearness_allowance)
            employee_data.append(house_rent_allowance)
            employee_data.append(travel_allowance)
            employee_data.append(washing_clothes_allowance)
            employee_data.append(total_allowance)
            employee_data.append(group_insurance)
            employee_data.append(bussiness_tax)
            employee_data.append(NPS_employee_contribution)
            employee_data.append(GPF_deduction)
            employee_data.append(GPF_loan_deduction)
            employee_data.append(life_insurance)
            employee_data.append(accidental_insurance)
            employee_data.append(np_employee_credit_union_deduction)
            employee_data.append(total_deduction)
            employee_data.append(in_hand)
            csv_data.append(employee_data)
            employee_data = []
       
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    csv_writer = csv.writer(response)
    for row in csv_data:
        csv_writer.writerow(row)

    return response



def ym_emp_report(request):



    year = request.GET.get('year')
    employee_id = request.GET.get('employee')

    if year == None:

        current_date = datetime.now()
        year = current_date.year


    print('year')
    print('year')
    print('year')
    print(year)

    if employee_id:

        employee_instance = employee.objects.get(id = employee_id)

        
       
        department_type_id= request.GET.get('department')
    
        print(department_type_id)

        if department_type_id:

            data = employee_salary.objects.filter(salary_date__year=year, employee__department__id__in = department_type_id, employee = employee_instance).order_by('salary_date')

        else:

            data = employee_salary.objects.filter(salary_date__year=year, employee = employee_instance).order_by('salary_date')
        
        


        employee_data = []
        for emp in data:
            given_date = emp.salary_date
            allowance_instance = emp.employee.employee_allo.all()
            dearness_allowance = allowance_instance.filter(allowance__name = 'Dearness Allowance').aggregate(Sum('amount'))['amount__sum'] or 0
            house_rent_allowance = allowance_instance.filter(allowance__name = 'House Rent').aggregate(Sum('amount'))['amount__sum'] or 0
            travel_allowance = allowance_instance.filter(allowance__name = 'Travel').aggregate(Sum('amount'))['amount__sum'] or 0
            washing_clothes_allowance = allowance_instance.filter(allowance__name = 'Washing Clothes').aggregate(Sum('amount'))['amount__sum'] or 0
            total_allowance = allowance_instance.aggregate(total=Sum('amount'))['total'] or 0
            
            total_dcps = employee_instance.dcps

            increment = employee_increament.objects.filter(employee=emp.employee,incerement_date__lte=datetime(given_date.year, given_date.month, 1)).order_by('-incerement_date').first()

            if increment:
                basic_salary = increment.new_basic
            else:
                basic_salary = emp.employee.basic_salary
            
            employee_data.append({
                    'employee': emp,
                    'total_allowance': total_allowance,
                    'dearness_allowance': dearness_allowance,
                    'house_rent_allowance': house_rent_allowance,
                    'travel_allowance': travel_allowance,
                    'washing_clothes_allowance': washing_clothes_allowance,
                    'travel_allowance': travel_allowance,
                    'total_allowance': total_allowance,
                    'total_dcps': total_dcps,
                    'basic_salary': basic_salary,
                })

    else:

        print('---------------------')
        print('---------------------')
        print('---------------------')

        employee_data = None

    context = {
        'employee_salary_filter' : employee_salary_filter(),
        'data': employee_data,
        'year': year,
        }



    print(context['data'])


    return render(request, 'report/ym_emp_report.html', context)



def download_ym_emp_report_csv(request):





    

    year = request.GET.get('year')
    employee_id = request.GET.get('employee')

    if year == None:

        current_date = datetime.now()
        year = current_date.year


    print('year')
    print('year')
    print('year')
    print(year)

    if employee_id:

        employee_instance = employee.objects.get(id = employee_id)

        
       
        department_type_id= request.GET.get('department')
    
        print(department_type_id)

        if department_type_id:

            data = employee_salary.objects.filter(salary_date__year=year, employee__department__id__in = department_type_id, employee = employee_instance).order_by('salary_date')

        else:

            data = employee_salary.objects.filter(salary_date__year=year, employee = employee_instance).order_by('salary_date')
        
        


        csv_data = []
        employee_data = []


        employee_data.append('Name')
        employee_data.append('Department')
        employee_data.append('Designation')
        employee_data.append('Absent days')
        employee_data.append('Basic Salary')
        employee_data.append('Dearness Allowance')
        employee_data.append('House Rent')
        employee_data.append('Travel')
        employee_data.append('Washing Clothes')
        employee_data.append('Total Allowances')
        employee_data.append('Total DCPS')
        csv_data.append(employee_data)
        employee_data = []


        for emp in data:
            given_date = emp.salary_date
            allowance_instance = emp.employee.employee_allo.all()
            dearness_allowance = allowance_instance.filter(allowance__name = 'Dearness Allowance').aggregate(Sum('amount'))['amount__sum'] or 0
            house_rent_allowance = allowance_instance.filter(allowance__name = 'House Rent').aggregate(Sum('amount'))['amount__sum'] or 0
            travel_allowance = allowance_instance.filter(allowance__name = 'Travel').aggregate(Sum('amount'))['amount__sum'] or 0
            washing_clothes_allowance = allowance_instance.filter(allowance__name = 'Washing Clothes').aggregate(Sum('amount'))['amount__sum'] or 0
            total_allowance = allowance_instance.aggregate(total=Sum('amount'))['total'] or 0
            
            total_dcps = employee_instance.dcps

            increment = employee_increament.objects.filter(employee=emp.employee,incerement_date__lte=datetime(given_date.year, given_date.month, 1)).order_by('-incerement_date').first()

            if increment:
                basic_salary = increment.new_basic
            else:
                basic_salary = emp.employee.basic_salary
            
            employee_data.append(str(emp.employee.name) + ' ' + str(emp.employee.middle_name) + ' ' + str(emp.employee.last_name))
            employee_data.append(emp.employee.department)
            employee_data.append(emp.employee.designation)
            employee_data.append(3)
            employee_data.append(basic_salary)
            employee_data.append(dearness_allowance)
            employee_data.append(house_rent_allowance)
            employee_data.append(travel_allowance)
            employee_data.append(washing_clothes_allowance)
            employee_data.append(total_allowance)
            employee_data.append(total_dcps)

            csv_data.append(employee_data)
            employee_data = []
    else:

        csv_data = None


    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    csv_writer = csv.writer(response)
    for row in csv_data:
        csv_writer.writerow(row)

    return response