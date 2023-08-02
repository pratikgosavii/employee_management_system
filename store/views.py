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
def get_company_goods_ajax(request):

    data = []
    

    if request.method == "POST":
        company_id = request.POST['company_id']
        try:
            instance = company.objects.filter(id = company_id).first()
            dropdown1 = company_goods.objects.filter(company = instance)
        except Exception:
            data['error_message'] = 'error'
            return JsonResponse(data)
        return JsonResponse(list(dropdown1.values('id', 'name')), safe = False) 


@login_required(login_url='login')
def get_goods_company_ajax(request):

    data = []

    if request.method == "POST":
        company_id = request.POST['company_id']
        company_goods_id = request.POST['company_goods']
        try:
            company_instance = company.objects.get(id= company_id)
            instance = company_goods.objects.filter(id = company_goods_id).first()
            dropdown1 = goods_company.objects.filter(company_goods = instance, company_name= company_instance)
        except Exception:
            data['error_message'] = 'error'
            return JsonResponse(data)
        return JsonResponse(list(dropdown1.values('id', 'goods_company_name')), safe = False) 


@login_required(login_url='login')
def get_agent_company_ajax(request):

    data = []
    print('i am here2')

    if request.method == "POST":
        company_id = request.POST['company_id']
        print(company_id)
        try:
            company_instance = company.objects.get(id= company_id)
            print(company_instance)
            
            agent_data = agent.objects.filter(company = company_instance)
            print(agent_data)
        except Exception:
            data['error_message'] = 'error'
            return JsonResponse(data)
        return JsonResponse(list(agent_data.values('id', 'name')), safe = False) 


@login_required(login_url='login')
def get_category_ajax(request):

    data = []
    print('i am here2')

    if request.method == "POST":
        company_goods_id = request.POST['company_goods_id']
        print(company_goods_id)
        try:
            company_goods_instance = goods_company.objects.filter(category__id = company_goods_id)
            print(company_goods_instance)
            
         
        except Exception:
            data['error_message'] = 'error'
            return JsonResponse(data)
        return JsonResponse(list(company_goods_instance.values('id', 'goods_company_name')), safe = False) 



@login_required(login_url='login')
def add_godown(request):

    if request.method == 'POST':

        forms = godown_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_godown')
        else:
            print(forms.errors)
    
    else:

        forms = godown_Form()

        context = {
            'form': forms
        }
        return render(request, 'store/add_godown.html', context)

        

@login_required(login_url='login')
def update_godown(request, godown_id):

    if request.method == 'POST':

        instance = godown.objects.get(id=godown_id)

        forms = godown_Form(request.POST, instance=instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_godown')
        else:
            print(forms.errors)
    
    else:

        instance = godown.objects.get(id=godown_id)
        forms = godown_Form(instance=instance)

        context = {
            'form': forms
        }
        return render(request, 'store/add_godown.html', context)

        

@login_required(login_url='login')
def delete_godown(request, godown_id):

    godown.objects.get(id=godown_id).delete()

    request.session['godown'] = None

    return HttpResponseRedirect(reverse('list_company_delete'))


        

@login_required(login_url='login')
def list_godown(request):

    data = godown.objects.all()

    context = {
        'data': data
    }

    return render(request, 'store/list_godown.html', context)


@login_required(login_url='login')
def add_customer(request):

    if request.method == 'POST':

        forms = customer_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_customer')
        else:
            print(forms.errors)
    
    else:

        forms = customer_Form()

        context = {
            'form': forms
        }
        return render(request, 'store/add_customer.html', context)

        

@login_required(login_url='login')
def update_customer(request, customer_id):

    if request.method == 'POST':

        instance = customer.objects.get(id=customer_id)

        forms = customer_Form(request.POST, instance=instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_customer')
        else:
            print(forms.errors)
    
    else:

        instance = customer.objects.get(id=customer_id)
        forms = customer_Form(instance=instance)

        context = {
            'form': forms
        }
        return render(request, 'store/add_customer.html', context)

        

@login_required(login_url='login')
def delete_customer(request, customer_id):

    customer.objects.get(id=customer_id).delete()

    request.session['customer'] = None

    return HttpResponseRedirect(reverse('list_company_delete'))


@login_required(login_url='login')
def list_customer(request):

    data = customer.objects.all()
    context = {
        'data': data
    }
    return render(request, 'store/list_customer.html', context)

        

@login_required(login_url='login')
def list_godown(request):

    data = godown.objects.all()

    context = {
        'data': data
    }

    return render(request, 'store/list_godown.html', context)


@login_required(login_url='login')
def add_dealer(request):

    if request.method == 'POST':

        forms = dealer_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_dealer')
        else:
            print(forms.errors)
    
    else:

        forms = dealer_Form()

        context = {
            'form': forms
        }
        return render(request, 'store/add_dealer.html', context)

        

@login_required(login_url='login')
def update_dealer(request, dealer_id):

    if request.method == 'POST':

        instance = dealer.objects.get(id=dealer_id)

        forms = dealer_Form(request.POST, instance=instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_dealer')
        else:
            print(forms.errors)
    
    else:

        instance = dealer.objects.get(id=dealer_id)
        forms = dealer_Form(instance=instance)

        context = {
            'form': forms
        }
        return render(request, 'store/add_dealer.html', context)

        

@login_required(login_url='login')
def delete_dealer(request, dealer_id):

    dealer.objects.get(id=dealer_id).delete()

    request.session['dealer'] = None

    return HttpResponseRedirect(reverse('list_company_delete'))


        

@login_required(login_url='login')
def list_dealer(request):

    data = dealer.objects.all()

    context = {
        'data': data
    }

    return render(request, 'store/list_dealer.html', context)



# @login_required(login_url='login')
# def add_company(request):

#     if request.method == 'POST':

#         forms = company_Form(request.POST)

#         if forms.is_valid():
#             forms.save()
#             return redirect('list_company')
#         else:
#             print(forms.errors)
    
#     else:

#         forms = company_Form()

#         context = {
#             'form': forms
#         }
#         return render(request, 'store/add_company.html', context)

        

# @login_required(login_url='login')
# def update_company(request, company_id):

#     if request.method == 'POST':

#         instance = company.objects.get(id=company_id)

#         forms = company_Form(request.POST, instance=instance)

#         if forms.is_valid():
#             forms.save()
#             return redirect('list_company')
#         else:
#             print(forms.errors)
    
#     else:

#         instance = company.objects.get(id=company_id)
#         forms = company_Form(instance=instance)

#         context = {
#             'form': forms
#         }
#         return render(request, 'store/add_company.html', context)

        

# @login_required(login_url='login')
# def delete_company(request, company_id):

#     company.objects.get(id=company_id).delete()

#     return HttpResponseRedirect(reverse('list_company_delete'))


        

# @login_required(login_url='login')
# def list_company(request):

#     data = company.objects.all()

#     context = {
#         'data': data
#     }

#     return render(request, 'store/list_company.html', context)



@login_required(login_url='login')
def add_category(request):
    
    if request.method == 'POST':

        forms = category_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_category')
        else:
            print(forms.errors)
            return redirect('add_category')
    
    else:

        forms = category_Form()

            
       
        context = {
            'form': forms,
           
        }

        return render(request, 'store/add_category.html', context)


def update_category(request, category_id):

    if request.method == 'POST':

        instance = category.objects.get(id=category_id)

        forms = category_Form(request.POST, instance = instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_category')

        else:
            print(forms.errors)
    
    else:

        instance = category.objects.get(id=category_id)

        forms = category_Form(instance = instance)


        context = {
            'form': forms,
            
        }

        return render(request, 'store/add_category.html', context)


@login_required(login_url='login')
def delete_category(request, category_id):
    
    category.objects.get(id=category_id).delete()

    return HttpResponseRedirect(reverse('list_category_delete'))


@login_required(login_url='login')
def list_category(request):

    
     
    data = category.objects.all().order_by('name')

    context = {
            'data': data
        }


    return render(request, 'store/list_category.html', context)



@login_required(login_url='login')
def add_size(request):
    
    if request.method == 'POST':

        forms = size_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_size')
        else:
            print(forms.errors)
            return redirect('list_size')
    
    else:

        forms = size_Form()
        
        grade_data = grade.objects.all()

        
        context = {
            'form': forms,
            'grade_data': grade_data,
        }

        return render(request, 'store/add_size.html', context)

@login_required(login_url='login')
def update_size(request, company_goods_id):

    if request.method == 'POST':

        instance = size.objects.get(id=company_goods_id)

        forms = size_Form(request.POST, instance = instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_size')
    
    else:

        instance = size.objects.get(id=company_goods_id)

        

        forms = size_Form(instance = instance)

        context = {
            'form': forms,
        }

        return render(request, 'store/add_size.html', context)


@login_required(login_url='login')
def delete_size(request, company_goods_id):
    
    size.objects.get(id=company_goods_id).delete()

    return HttpResponseRedirect(reverse('list_size_delete'))


@login_required(login_url='login')
def list_size(request):
    
     
    data = size.objects.all().order_by('name')

    context = {
            'data': data
        }


    return render(request, 'store/list_size.html', context)



@login_required(login_url='login')
def add_grade(request):
    
    if request.method == 'POST':

        forms = grade_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_grade')
        else:
            print(forms.errors)
            return redirect('list_grade')
    
    else:

        forms = grade_Form()
      
        grade_data = grade.objects.all()

        
        context = {
            'form': forms,
            'grade_data': grade_data,
        }

        return render(request, 'store/add_grade.html', context)

@login_required(login_url='login')
def update_grade(request, company_goods_id):

    if request.method == 'POST':

        instance = grade.objects.get(id=company_goods_id)

        forms = grade_Form(request.POST, instance = instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_grade')
    
    else:

        instance = grade.objects.get(id=company_goods_id)

        

        forms = grade_Form(instance = instance)

        context = {
            'form': forms,
        }

        return render(request, 'store/add_grade.html', context)


@login_required(login_url='login')
def delete_grade(request, company_goods_id):
    
    grade.objects.get(id=company_goods_id).delete()

    return HttpResponseRedirect(reverse('list_grade_delete'))


@login_required(login_url='login')
def list_grade(request):
    
     
    data = grade.objects.all().order_by('name')

    context = {
            'data': data
        }


    return render(request, 'store/list_grade.html', context)

@login_required(login_url='login')
def add_thickness(request):
    
    if request.method == 'POST':

        forms = thickness_Form(request.POST)

        if forms.is_valid():
            forms.save()
            return redirect('list_thickness')
        else:
            print(forms.errors)
            return redirect('list_thickness')
    
    else:

        forms = thickness_Form()
        
        grade_data = grade.objects.all()

        
        context = {
            'form': forms,
            'grade_data': grade_data,
        }

        return render(request, 'store/add_thickness.html', context)

@login_required(login_url='login')
def update_thickness(request, company_goods_id):

    if request.method == 'POST':

        instance = thickness.objects.get(id=company_goods_id)

        forms = thickness_Form(request.POST, instance = instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_thickness')
    
    else:

        instance = thickness.objects.get(id=company_goods_id)

        

        forms = thickness_Form(instance = instance)

        context = {
            'form': forms,
        }

        return render(request, 'store/add_thickness.html', context)


@login_required(login_url='login')
def delete_thickness(request, thickness_id):
    
    thickness.objects.get(id=thickness_id).delete()

    return HttpResponseRedirect(reverse('list_thickness_delete'))


@login_required(login_url='login')
def list_thickness(request):
    
    data = thickness.objects.all().order_by('name')

    context = {
            'data': data
        }


    return render(request, 'store/list_thickness.html', context)





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

        instance = pay_scale.objects.get(id=company_goods_id)

        

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
def update_designation(request, designation_id):

    if request.method == 'POST':

        instance = designation.objects.get(id=designation_id)

        forms = designation_Form(request.POST, instance = instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_designation')
    
    else:

        instance = designation.objects.get(id=designation_id)

        

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





@login_required(login_url='login')
def add_employee(request):
    
    if request.method == 'POST':

        forms = employee_Form(request.POST)

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

