# Generated by Django 4.1.5 on 2023-08-09 13:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0039_alter_employee_da_alter_employee_date_of_retirement_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='courtesy_titles',
            field=models.CharField(blank=True, choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Miss', 'Mrs'), ('Ms', 'Ms'), ('Dr', 'Dr')], max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_of_retirement',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 9, 18, 41, 55, 710616), null=True),
        ),
    ]
