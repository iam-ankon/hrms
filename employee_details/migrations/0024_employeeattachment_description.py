# Generated by Django 5.1.6 on 2025-03-06 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_details', '0023_remove_employeeattachment_custom_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeattachment',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
