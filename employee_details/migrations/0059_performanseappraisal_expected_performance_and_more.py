# Generated by Django 5.1.6 on 2025-03-28 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_details', '0058_remove_performanseappraisal_appraisal_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='performanseappraisal',
            name='expected_performance',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='performanseappraisal',
            name='increment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='performanseappraisal',
            name='performance_reward',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='performanseappraisal',
            name='present_designation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='performanseappraisal',
            name='present_salary',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='performanseappraisal',
            name='promotion',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='performanseappraisal',
            name='proposed_designation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='performanseappraisal',
            name='proposed_salary',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
