# Generated by Django 5.1.6 on 2025-04-15 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_details', '0075_alter_employeedetails_image1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedetails',
            name='department',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='employeedetails',
            name='job_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='employeedetails',
            name='mail_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employeedetails',
            name='office_phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeedetails',
            name='permanent_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employeedetails',
            name='personal_phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
