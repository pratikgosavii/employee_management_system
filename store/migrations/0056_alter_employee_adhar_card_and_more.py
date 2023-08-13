# Generated by Django 4.1.5 on 2023-08-13 17:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0055_alter_employee_adhar_card_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='adhar_card',
            field=models.IntegerField(blank=True, max_length=12, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_of_retirement',
            field=models.DateField(default=datetime.datetime(2023, 8, 13, 22, 33, 51, 63854)),
        ),
    ]