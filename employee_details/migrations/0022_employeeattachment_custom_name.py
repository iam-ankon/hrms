# Generated by Django 5.1.6 on 2025-03-06 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_details', '0021_employeeattachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeattachment',
            name='custom_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
