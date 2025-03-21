# Generated by Django 5.1.6 on 2025-03-05 08:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_details', '0020_attendance_office_start_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeAttachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='employee_attachments/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='employee_details.employeedetails')),
            ],
        ),
    ]
