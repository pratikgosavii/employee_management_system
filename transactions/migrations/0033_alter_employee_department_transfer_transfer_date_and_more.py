# Generated by Django 4.1.5 on 2023-08-09 09:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0032_remove_employee_salary_department_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_department_transfer',
            name='transfer_date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 9, 14, 31, 49, 600278), null=True),
        ),
        migrations.AlterField(
            model_name='employee_increament',
            name='incerement_date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 9, 14, 31, 49, 602335), null=True),
        ),
        migrations.AlterField(
            model_name='leaves',
            name='date_from',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 9, 14, 31, 49, 603292), null=True),
        ),
        migrations.AlterField(
            model_name='leaves',
            name='date_to',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 9, 14, 31, 49, 603292), null=True),
        ),
    ]
