# Generated by Django 5.1.6 on 2025-03-25 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_details', '0054_interview_current_remuneration_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='final_selection_remakrs',
            field=models.TextField(blank=True, null=True),
        ),
    ]
