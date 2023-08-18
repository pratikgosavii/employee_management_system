# Generated by Django 4.1.5 on 2023-08-17 00:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0063_alter_employee_department_transfer_transfer_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee_total_leaves',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default=datetime.datetime(2023, 8, 17, 6, 5, 50, 305555), null=True)),
                ('working_days', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='employee_department_transfer',
            name='transfer_date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 17, 6, 5, 50, 282467), null=True),
        ),
        migrations.AlterField(
            model_name='employee_increament',
            name='incerement_date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 17, 6, 5, 50, 282988), null=True),
        ),
        migrations.AlterField(
            model_name='leaves',
            name='date_from',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 17, 6, 5, 50, 305555), null=True),
        ),
        migrations.AlterField(
            model_name='leaves',
            name='date_to',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 17, 6, 5, 50, 305555), null=True),
        ),
    ]