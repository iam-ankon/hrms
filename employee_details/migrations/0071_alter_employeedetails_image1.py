# Generated by Django 5.1.6 on 2025-04-09 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_details', '0070_employeeleavebalance_employee_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedetails',
            name='image1',
            field=models.BinaryField(),
        ),
    ]
