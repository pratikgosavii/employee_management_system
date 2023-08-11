# Generated by Django 4.1.5 on 2023-08-11 00:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0051_alter_employee_date_of_retirement'),
        ('transactions', '0049_alter_employee_deduction_employee_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_department_transfer',
            name='transfer_date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 11, 6, 8, 5, 867278), null=True),
        ),
        migrations.AlterField(
            model_name='employee_increament',
            name='incerement_date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 11, 6, 8, 5, 868321), null=True),
        ),
        migrations.AlterField(
            model_name='employee_loan',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_loan_re', to='store.employee'),
        ),
        migrations.AlterField(
            model_name='employee_miscellaneous_deduction',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_misc', to='store.employee'),
        ),
        migrations.AlterField(
            model_name='leaves',
            name='date_from',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 11, 6, 8, 5, 869320), null=True),
        ),
        migrations.AlterField(
            model_name='leaves',
            name='date_to',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 11, 6, 8, 5, 869320), null=True),
        ),
    ]
