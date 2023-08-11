# Generated by Django 4.1.5 on 2023-08-11 18:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0050_alter_employee_department_transfer_transfer_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_department_transfer',
            name='transfer_date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 11, 23, 49, 8, 366463), null=True),
        ),
        migrations.AlterField(
            model_name='employee_increament',
            name='incerement_date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 11, 23, 49, 8, 367464), null=True),
        ),
        migrations.AlterField(
            model_name='leaves',
            name='date_from',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 11, 23, 49, 8, 368463), null=True),
        ),
        migrations.AlterField(
            model_name='leaves',
            name='date_to',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 11, 23, 49, 8, 368463), null=True),
        ),
    ]
