# Generated by Django 4.1.5 on 2023-08-17 00:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0064_alter_employee_date_of_retirement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_of_retirement',
            field=models.DateField(default=datetime.datetime(2023, 8, 17, 6, 5, 50, 233471)),
        ),
    ]
