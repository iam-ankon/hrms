# Generated by Django 5.1.6 on 2025-03-08 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_details', '0026_alter_tadgroup_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedetails',
            name='image1',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
