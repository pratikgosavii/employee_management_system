# Generated by Django 4.1.5 on 2023-08-09 20:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0043_alter_employee_date_of_retirement_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_of_retirement',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 10, 2, 19, 29, 847993), null=True),
        ),
    ]