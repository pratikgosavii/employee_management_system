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

    path('add-employee-transfer-department/', add_employee_transfer_department, name='employee_add_transfer_departmen'),
    # path('update-employee-transfer-department/<employee_transfer_department_id>', update_employee_transfer_department, name='update_employee_transfer_departmen'),
    path('employee-transfer-department/', list_employee_transfer_department, name='list_employee_transfer_department'),

    path('add-employee-increment/', add_employee_increment, name='employee_add_salary_increament'),
    # path('update-employee-increment/<employee_increment_id>', update_increment, name='update_transfer_departmen'),
    path('employee-increment/', list_increment, name='list_increment'),

    path('post-vacancy/', post_vacancy, name='post_vacancy'),
    path('update-vacancy/<vacancy_id>', update_vacancy, name='update_vacancy'),
    path('delete-vacancy/<vacancy_id>', delete_vacancy, name='delete_vacancy'),
    path('list-vacancy/', list_vacancy, name='list_vacancy'),


    path('get_old_department_ajaxy/', get_old_department_ajax, name='get_old_department_ajax'),
    path('get_old_basic_ajax/', get_old_basic_ajax, name='get_old_basic_ajax'),
    



]