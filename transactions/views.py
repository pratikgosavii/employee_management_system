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

        print(request.POST)

       


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

    employee_instance = employee.objects.get(id = employee_id)

    
    if request.method == 'POST':

        updated_request = request.POST.copy()
        updated_request.update({'employee': employee_instance})

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
    
    employee_allowance.objects.get(id=employee_allowance_id).delete()

    return HttpResponseRedirect(reverse('list_employee_allowance_delete'))


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

    employee_instance = employee.objects.get(id = employee_id)

    
    if request.method == 'POST':

        updated_request = request.POST.copy()
        updated_request.update({'employee': employee_instance})

        forms = employee_deduction_Form(updated_request)

        if forms.is_valid():
            forms.save()

            return redirect('manage_salary', employee_id = employee_id)
        else:
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
    
    employee_deduction.objects.get(id=employee_deduction_id).delete()

    return HttpResponseRedirect(reverse('list_employee_deduction_delete'))


@login_required(login_url='login')
def list_employee_deduction(request):
    
     
    data = employee_deduction.objects.all().order_by('name')

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
    
    employee_loan.objects.get(id=employee_loan_id).delete()

    return HttpResponseRedirect(reverse('list_employee_loan_delete'))


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
    
    employee_miscellaneous_deduction.objects.get(id=employee_miscellaneous_deduction_id).delete()

    return HttpResponseRedirect(reverse('list_employee_miscellaneous_deduction_delete'))


@login_required(login_url='login')
def list_employee_miscellaneous_deduction(request):
    
     
    data = employee_miscellaneous_deduction.objects.all().order_by('name')

    context = {
            'data': data
        }


    return render(request, 'store/list_employee_miscellaneous_deduction.html', context)

