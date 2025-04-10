# Generated by Django 5.1.6 on 2025-04-08 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_details', '0063_employeeleave_actual_date_of_joining_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeleave',
            name='employee_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeeleave',
            name='balance',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='employeeleave',
            name='leave_applied_for',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='employeeleave',
            name='leave_availed',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='employeeleave',
            name='leave_entited',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='employeeleave',
            name='status',
            field=models.CharField(blank=True, choices=[('approved', 'Approved'), ('pending', 'Pending'), ('rejected', 'Rejected')], default='pending', max_length=50, null=True),
        ),
    ]
