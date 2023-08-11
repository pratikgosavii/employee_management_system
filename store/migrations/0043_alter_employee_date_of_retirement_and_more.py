# Generated by Django 4.1.5 on 2023-08-09 20:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0042_alter_employee_date_of_retirement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_of_retirement',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 10, 2, 1, 19, 808337), null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
    ]