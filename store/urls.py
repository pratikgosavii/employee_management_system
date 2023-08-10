from django.urls import path

from .views import *
from store import views

urlpatterns = [

    #delete urls 

    path('add-pay-scale/', add_pay_scale, name='add_pay_scale'),
    path('update-pay-scale/<pay_scale_id>', update_pay_scale, name='update_pay_scale'),
    path('delete-pay-scale/<pay_scale_id>', delete_pay_scale, name='delete_pay_scale'),
    path('list-pay-scale/', list_pay_scale, name='list_pay_scale'),

    path('add-grade-pay/', add_grade_pay, name='add_grade_pay'),
    path('update-grade-pay/<grade_pay_id>', update_grade_pay, name='update_grade_pay'),
    path('delete-grade-pay/<grade_pay_id>', delete_grade_pay, name='delete_grade_pay'),
    path('list-grade-pay/', list_grade_pay, name='list_grade_pay'),

    path('add-grade-payment/', add_grade_payment, name='add_grade_payment'),
    path('update-grade-payment/<grade_payment_id>', update_grade_payment, name='update_grade_payment'),
    path('delete-grade-payment/<grade_payment_id>', delete_grade_payment, name='delete_grade_payment'),
    path('list-grade-payment/', list_grade_payment, name='list_grade_payment'),

    path('add-employee-type/', add_employee_type, name='add_employee_type'),
    path('update-employee-type/<employee_type_id>', update_employee_type, name='update_employee_type'),
    path('delete-employee-type/<employee_type_id>', delete_employee_type, name='delete_employee_type'),
    path('list-employee-type/', list_employee_type, name='list_employee_type'),

    path('add-department-type/', add_department_type, name='add_department_type'),
    path('update-department-type/<department_type_id>', update_department_type, name='update_department_type'),
    path('delete-department-type/<department_type_id>', delete_department_type, name='delete_department_type'),
    path('list-department-type/', list_department_type, name='list_department_type'),

    path('add-designation/', add_designation, name='add_designation'),
    path('update-designation/<designation_type_id>', update_designation, name='update_designation'),
    path('delete-designation/<designation_type_id>', delete_designation, name='delete_designation'),
    path('list-designation/', list_designation, name='list_designation'),

    path('add-emp_classes/', add_emp_classes, name='add_emp_classes'),
    path('update-emp_classes/<emp_classes_type_id>', update_emp_classes, name='update_emp_classes'),
    path('delete-emp_classes/<emp_classes_type_id>', delete_emp_classes, name='delete_emp_classes'),
    path('list-emp_classes/', list_emp_classes, name='list_emp_classes'),

    path('add-bank/', add_bank, name='add_bank'),
    path('update-bank/<bank_type_id>', update_bank, name='update_bank'),
    path('delete-bank/<bank_type_id>', delete_bank, name='delete_bank'),
    path('list-bank/', list_bank, name='list_bank'),

    path('add-loan/', add_loan, name='add_loan'),
    path('update-loan/<loan_type_id>', update_loan, name='update_loan'),
    path('delete-loan/<loan_type_id>', delete_loan, name='delete_loan'),
    path('list-loan/', list_loan, name='list_loan'),


    path('add-employee/', add_employee, name='add_employee'),
    path('update-employee/<employee_id>', update_employee, name='update_employee'),
    path('delete-employee/<employee_id>', delete_employee, name='delete_employee'),
    path('list-employee/', list_employee, name='list_employee'),
    path('get-employee-retiredmentdate', retiredmentdate, name='retiredmentdate'),

    path('add-allowance/', add_allowance, name='add_allowance'),
    path('update-allowance/<allowance_id>', update_allowance, name='update_allowance'),
    path('delete-allowance/<allowance_id>', delete_allowance, name='delete_allowance'),
    path('list-allowance/', list_allowance, name='list_allowance'),

    path('add-deduction/', add_deduction, name='add_deduction'),
    path('update-deduction/<deduction_id>', update_deduction, name='update_deduction'),
    path('delete-deduction/<deduction_id>', delete_deduction, name='delete_deduction'),
    path('list-deduction/', list_deduction, name='list_deduction'),

    path('add-miscellaneous_deduction/', add_miscellaneous_deduction, name='add_miscellaneous_deduction'),
    path('update-miscellaneous_deduction/<miscellaneous_deduction_id>', update_miscellaneous_deduction, name='update_miscellaneous_deduction'),
    path('delete-miscellaneous_deduction/<miscellaneous_deduction_id>', delete_miscellaneous_deduction, name='delete_miscellaneous_deduction'),
    path('list-miscellaneous_deduction/', list_miscellaneous_deduction, name='list_miscellaneous_deduction'),





    # path('add-employee/', add_employee, name='add_employee'),
    # path('update-employee/<employee_id>', update_employee, name='update_employee'),
    # path('delete-employee/<employee_id>', delete_employee, name='delete_employee'),
    # path('list-employee/', list_employee, name='list_employee'),


    # 
    # 
    # 
    # 
    # 

]
