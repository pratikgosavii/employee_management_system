# Generated by Django 4.1.5 on 2023-08-19 03:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0071_alter_employee_department_transfer_transfer_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_allowance',
            name='amount',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='employee_deduction',
            name='amount',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='employee_department_transfer',
            name='transfer_date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 19, 8, 52, 48, 818463), null=True),
        ),
        migrations.AlterField(
            model_name='employee_increament',
            name='incerement_date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 19, 8, 52, 48, 818463), null=True),
        ),
        migrations.AlterField(
            model_name='employee_loan',
            name='amount',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='leaves',
            name='date_from',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 19, 8, 52, 48, 819465), null=True),
        ),
        migrations.AlterField(
            model_name='leaves',
            name='date_to',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 19, 8, 52, 48, 819465), null=True),
        ),
        migrations.AlterField(
            model_name='month_working_days',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 19, 8, 52, 48, 831328), null=True),
        ),
    ]
