# Generated by Django 4.1.5 on 2023-08-11 00:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0049_alter_allowance_is_fixed_alter_deduction_is_fixed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_of_retirement',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 11, 5, 37, 32, 830423), null=True),
        ),
    ]