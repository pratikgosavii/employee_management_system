from django import forms
from django.forms.widgets import DateInput

from .models import *
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime


class employee_allowance_Form(forms.ModelForm):
    class Meta:
        model = employee_allowance
        fields = '__all__'
        widgets = {
          
            'employee': forms.Select(attrs={
                'class': 'form-control', 'id': 'employee'
            }),
            'allowance': forms.Select(attrs={
                'class': 'form-control', 'id': 'allowance'
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'amount'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'description'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control', 'id': 'status'
            }),
           
            
        }




from django.forms.widgets import DateTimeInput



class employee_deduction_Form(forms.ModelForm):


    
    class Meta:
        model = employee_deduction
        fields = '__all__'
        widgets = {
          
            'employee': forms.Select(attrs={
                'class': 'form-control', 'id': 'employee'
            }),
            'deduction': forms.Select(attrs={
                'class': 'form-control', 'id': 'deduction'
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'amount'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'description'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control', 'id': 'status'
            }),



            
            
           
            
        }

class employee_loan_Form(forms.ModelForm):
    class Meta:
        model = employee_loan
        fields = '__all__'
        widgets = {
          
            'employee': forms.Select(attrs={
                'class': 'form-control', 'id': 'employee'
            }),
            'loan': forms.Select(attrs={
                'class': 'form-control', 'id': 'loan'
            }),
            'total_loan_amount': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'amount'
            }),
            'loan_percentage': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'amount'
            }),
            'year': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'amount'
            }),
            'emi': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'amount'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'description'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control', 'id': 'status'
            }),
            'date': DateTimeInput(attrs={'type': 'date', 'class' : 'date_css'}, format = '%Y-%m-%d'),
           
            
        }

class employee_miscellaneous_deduction_Form(forms.ModelForm):
    class Meta:
        model = employee_miscellaneous_deduction
        fields = '__all__'
        widgets = {
          
            'employee': forms.Select(attrs={
                'class': 'form-control', 'id': 'employee'
            }),
            'miscellaneous': forms.Select(attrs={
                'class': 'form-control', 'id': 'deduction'
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'amount'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'description'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control', 'id': 'status'
            }),

            'date': DateInput(attrs={ 'class': 'form-control', 'type': 'date'}, format = '%Y-%m-%d'),
           
            
        }



        

class employee_department_transfer_Form(forms.ModelForm):
    class Meta:
        model = employee_department_transfer
        fields = '__all__'
        widgets = {
          
            'employee': forms.Select(attrs={
                'class': 'form-control', 'id': 'employee'
            }),
            'old_deparment': forms.Select(attrs={
                'class': 'form-control', 'id': 'old_deparment', 'disabled': 'disabled'
            }),
            'new_deparment': forms.Select(attrs={
                'class': 'form-control', 'id': 'deduction'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'description'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control', 'id': 'status'
            }),

            'transfer_date': DateInput(attrs={ 'class': 'form-control', 'type': 'date'}, format = '%Y-%m-%d'),
            
           
            
        }



        
        

class vacancy_Form(forms.ModelForm):
    class Meta:
        model = vacancy
        fields = '__all__'
        widgets = {
          
            'department': forms.Select(attrs={
                'class': 'form-control', 'id': 'employee'
            }),
            
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            
            'no_of_vacancy': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'description'
            }),
            
            'description': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'description'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control', 'id': 'status'
            }),

        }



        

class employee_increament_Form(forms.ModelForm):
    class Meta:
        model = employee_increament
        fields = '__all__'
        widgets = {
          
            'department': forms.Select(attrs={
                'class': 'form-control', 'id': 'department'
            }),
            
            'employee': forms.Select(attrs={
                'class': 'form-control', 'id': 'employee'
            }),
            
            'old_basic': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'old_basic', 'readonly' : 'readonly'
            }),

            'new_basic': forms.NumberInput(attrs={
                'class': 'form-control custo', 'id': 'new_basic'
            }),
            
            'description': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'description'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control', 'id': 'status'
            }),

            'incerement_date': DateInput(attrs={ 'class': 'form-control', 'type': 'date'}, format = '%Y-%m-%d'),


        }



        
        

class leaves_Form(forms.ModelForm):
    class Meta:
        model = leaves
        fields = '__all__'
        widgets = {
          
            'employee': forms.Select(attrs={
                'class': 'form-control', 'id': 'employee'
            }),
            'leave_type': forms.Select(attrs={
                'class': 'form-control', 'id': 'leave_type'
            }),
            'total_days': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'description'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'description'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control', 'id': 'status'
            }),

            'date_from': DateInput(attrs={ 'class': 'form-control', 'type': 'date'}, format = '%Y-%m-%d'),
            'date_to': DateInput(attrs={ 'class': 'form-control', 'type': 'date'}, format = '%Y-%m-%d'),


        }



    
from django.forms.widgets import DateTimeInput

    
class employee_salary_Form(forms.ModelForm):
    class Meta:
        model = employee_salary
        fields = '__all__'
        widgets = {
          
            'employee': forms.Select(attrs={
                'class': 'form-control', 'id': 'employee'
            }),
            'total_days': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'description'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'description'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control', 'id': 'status'
            }),

            'salary_date': DateTimeInput(attrs={'type': 'date', 'class' : 'date_css'}, format = '%Y-%m-%d'),


        }

