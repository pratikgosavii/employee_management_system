from django.urls import path

from .views import *
from store import views

urlpatterns = [


    
    path('manage-salary/<employee_id>', manage_salary, name='manage_salary'),
   
    path('add-employee-allowance/', add_employee_allowance, name='employee_add_allowance'),
    path('update-employee-allowance/<employee_allowance_id>', update_employee_allowance, name='update_employee_allowance'),
    path('delete-employee-allowance/<employee_allowance_id>', delete_employee_allowance, name='delete_employee_allowance'),
    path('list-employee-allowance/', list_employee_allowance, name='list_employee_allowance'),

    path('add-employee-deduction/', add_employee_deduction, name='employee_add_deduction'),
    path('update-employee-deduction/<employee_deduction_id>', update_employee_deduction, name='update_employee_deduction'),
    path('delete-employee-deduction/<employee_deduction_id>', delete_employee_deduction, name='delete_employee_deduction'),
    path('list-employee-deduction/', list_employee_deduction, name='list_employee_deduction'),

    path('add-employee-loan/', add_employee_loan, name='employee_add_loan'),
    path('update-employee-loan/<employee_loan_id>', update_employee_loan, name='update_employee_loan'),
    path('delete-employee-loan/<employee_loan_id>', delete_employee_loan, name='delete_employee_loan'),
    path('list-employee-loan/', list_employee_loan, name='list_employee_loan'),
    
    path('add-employee-miscellaneous-deduction/', add_employee_miscellaneous_deduction, name='employee_add_miscellaneous_deduction'),
    path('update-employee-miscellaneous-deduction/<employee_miscellaneous_deduction_id>', update_employee_miscellaneous_deduction, name='update_employee_miscellaneous_deduction'),
    path('delete-employee-miscellaneous-deduction/<employee_miscellaneous_deduction_id>', delete_employee_miscellaneous_deduction, name='delete_employee_miscellaneous_deduction'),
    path('list-employee-miscellaneous-deduction/', list_employee_miscellaneous_deduction, name='list_employee_miscellaneous_deduction'),


]