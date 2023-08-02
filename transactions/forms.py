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
           
            
        }



        
