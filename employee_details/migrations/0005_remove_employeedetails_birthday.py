# Generated by Django 5.1.6 on 2025-02-27 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_details', '0004_alter_employeedetails_emergency_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeedetails',
            name='birthday',
        ),
    ]
