# Generated by Django 5.1.6 on 2025-03-06 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_details', '0022_employeeattachment_custom_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeeattachment',
            name='custom_name',
        ),
    ]
