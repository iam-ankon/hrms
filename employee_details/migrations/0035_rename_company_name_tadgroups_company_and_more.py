# Generated by Django 5.1.6 on 2025-03-08 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_details', '0034_tadgroups'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tadgroups',
            old_name='company_name',
            new_name='company',
        ),
        migrations.RemoveField(
            model_name='tadgroups',
            name='group_name',
        ),
    ]
