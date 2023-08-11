import django_filters
from django_filters import DateFilter, CharFilter
from django.forms.widgets import DateInput
from django import forms

from store.models import *
from .forms import *

from django_filters import FilterSet, ChoiceFilter, NumberFilter


class employee_filter(django_filters.FilterSet):

    department = django_filters.ModelChoiceFilter(
        queryset=department_type.objects.all(),
        widget=forms.Select(
            attrs={
                'class' : 'form-control',
                'id' : 'department'
            })
    )
   
    year = NumberFilter(field_name='date_field', lookup_expr='year', label='Year', widget=forms.TextInput(attrs={'class': 'form-control'}))
    month = ChoiceFilter(choices=[(i, i) for i in range(1, 13)], method='filter_by_month', label='Month', widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = employee
        fields = '__all__'
       
   

class employee_salary_filter(django_filters.FilterSet):

    employee = django_filters.ModelChoiceFilter(
        queryset=employee.objects.all(),
        widget=forms.Select(
            attrs={
                'class' : 'form-control',
                'id' : 'emplloyee'
            })
    )
   
    department = django_filters.ModelChoiceFilter(
        queryset=department_type.objects.all(),
        widget=forms.Select(
            attrs={
                'class' : 'form-control',
                'id' : 'department'
            })
    )
   
    salary_date = DateFilter(field_name="salary_date", lookup_expr='gte', widget=forms.DateInput(
            attrs={
                'id': 'datepicker1212',
                'type': 'date',
                'class' : 'form-control date_css'
            }
        ))

    class Meta:
        model = employee_salary
        fields = '__all__'
       
   