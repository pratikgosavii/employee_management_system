# Generated by Django 4.1.5 on 2023-08-19 03:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0075_alter_allowance_amount_alter_deduction_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_of_retirement',
            field=models.DateField(default=datetime.datetime(2023, 8, 19, 9, 23, 24, 454706)),
        ),
    ]
