# Generated by Django 4.1.5 on 2023-08-10 20:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0045_alter_employee_adhar_card_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deduction',
            name='is_fixed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_of_retirement',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 11, 2, 5, 5, 325027), null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='permanent_address',
            field=models.TextField(blank=True, max_length=120, null=True, unique=True),
        ),
    ]
