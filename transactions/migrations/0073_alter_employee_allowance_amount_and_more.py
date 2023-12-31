# Generated by Django 4.1.5 on 2023-08-19 03:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0072_alter_employee_allowance_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_allowance',
            name='amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='employee_deduction',
            name='amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='employee_department_transfer',
            name='transfer_date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 19, 8, 54, 29, 451383), null=True),
        ),
        migrations.AlterField(
            model_name='employee_increament',
            name='incerement_date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 19, 8, 54, 29, 452371), null=True),
        ),
        migrations.AlterField(
            model_name='employee_loan',
            name='amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee_loan',
            name='total_loan_amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='leaves',
            name='date_from',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 19, 8, 54, 29, 452371), null=True),
        ),
        migrations.AlterField(
            model_name='leaves',
            name='date_to',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 19, 8, 54, 29, 452371), null=True),
        ),
        migrations.AlterField(
            model_name='month_working_days',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 19, 8, 54, 29, 467317), null=True),
        ),
    ]
