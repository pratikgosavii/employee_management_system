from django import forms

from .models import *
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from django.forms.widgets import DateInput


class employee_Form(forms.ModelForm):
    class Meta:
        model = employee
        fields = '__all__'
        widgets = {
          
          
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'middle_name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'taluka': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'district': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'state': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'country': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'pin_code': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),



            'adhar_card': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'pan_card': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'biometric_no': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'nps_dcps': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
        

            'department': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'employee_type': forms.Select(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'grade_payment': forms.Select(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'pay_scale': forms.Select(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'designation': forms.Select(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'grade_pay': forms.Select(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'basic_salary': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'date_of_birth': DateInput(attrs={ 'class': 'form-control', 'type': 'date'}, format = '%Y-%m-%d'),
            'date_of_joining': DateInput(attrs={ 'class': 'form-control', 'type': 'date'}, format = '%Y-%m-%d'),
            'date_of_retirement': DateInput(attrs={ 'class': 'form-control', 'type': 'date'}, format = '%Y-%m-%d'),
          

            'bank_ac_no': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'permanent_address': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),


       
            
        }

        def __init__(self, *args, **kwargs):
            super(employee_Form, self).__init__(*args, **kwargs)
            # Optional: You can add extra attributes to the fields here.
            self.fields['hra'].widget.attrs.update({'class': 'form-control'})
            self.fields['ta'].widget.attrs.update({'class': 'form-control'})
            self.fields['da'].widget.attrs.update({'class': 'form-control'})
            self.fields['physical_disable'].widget.attrs.update({'class': 'form-control'})
           





class pay_scale_Form(forms.ModelForm):
    class Meta:
        model = pay_scale
        fields = '__all__'
        widgets = {
          

            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control', 'id': 'categoryyy'
            }),
           
            
        }

class grade_pay_Form(forms.ModelForm):
    class Meta:
        model = grade_pay
        fields = '__all__'
        widgets = {
          

            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control', 'id': 'categoryyy'
            }),
           
            
        }

class grade_payment_Form(forms.ModelForm):
    class Meta:
        model = grade_payment
        fields = '__all__'
        widgets = {
          

            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control', 'id': 'categoryyy'
            }),
           
            
        }

class employee_type_Form(forms.ModelForm):
    class Meta:
        model = employee_type
        fields = '__all__'
        widgets = {
          

            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control', 'id': 'categoryyy'
            }),
           
            
        }

class department_type_Form(forms.ModelForm):
    class Meta:
        model = department_type
        fields = '__all__'
        widgets = {
          

            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control', 'id': 'categoryyy'
            }),
           
            
        }



class designation_Form(forms.ModelForm):
    class Meta:
        model = designation
        fields = '__all__'
        widgets = {
          

            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control', 'id': 'categoryyy'
            }),
           
            
        }

class emp_classes_Form(forms.ModelForm):
    class Meta:
        model = emp_classes
        fields = '__all__'
        widgets = {
          

            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control', 'id': 'categoryyy'
            }),
           
            
        }

class bank_Form(forms.ModelForm):
    class Meta:
        model = bank
        fields = '__all__'
        widgets = {
          

            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control', 'id': 'categoryyy'
            }),
           
            
        }

class loan_Form(forms.ModelForm):
    class Meta:
        model = loan
        fields = '__all__'
        widgets = {
          

            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'bank': forms.Select(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control', 'id': 'categoryyy'
            }),
           
            
        }



class miscellaneous_deduction_Form(forms.ModelForm):
    class Meta:
        model = miscellaneous_deduction
        fields = '__all__'
        widgets = {
          

            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'amount': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control', 'id': 'categoryyy'
            }),
           
            
        }




class allowance_Form(forms.ModelForm):
    class Meta:
        model = allowance
        fields = '__all__'
        widgets = {
          

            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'percentage': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'da_percentage': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control', 'id': 'categoryyy'
            }),
           
            
        }


        def __init__(self, *args, **kwargs):
            super(allowance_Form, self).__init__(*args, **kwargs)
            # Optional: You can add extra attributes to the fields here.
            self.fields['is_fixed'].widget.attrs.update({'class': 'form-control'})
            self.fields['da_percentage'].widget.attrs.update({'class': 'form-control'})
           

class deduction_Form(forms.ModelForm):
    class Meta:
        model = deduction
        fields = '__all__'
        widgets = {
          

            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'percentage': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'da_percentage': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control', 'id': 'categoryyy'
            }),
           
            
        }


        def __init__(self, *args, **kwargs):
            super(deduction_Form, self).__init__(*args, **kwargs)
            # Optional: You can add extra attributes to the fields here.
            self.fields['is_fixed'].widget.attrs.update({'class': 'form-control'})
            self.fields['da_percentage'].widget.attrs.update({'class': 'form-control'})
           
