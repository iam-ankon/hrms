# Generated by Django 5.1.6 on 2025-03-24 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_details', '0051_rename_cvmanagement_lettersend'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interview',
            name='clarity_of_communication',
        ),
        migrations.RemoveField(
            model_name='interview',
            name='cultural_fit',
        ),
        migrations.RemoveField(
            model_name='interview',
            name='english_proficiency',
        ),
        migrations.RemoveField(
            model_name='interview',
            name='feedback_provided',
        ),
        migrations.RemoveField(
            model_name='interview',
            name='good_behaviour',
        ),
        migrations.RemoveField(
            model_name='interview',
            name='interviewee_confirmed',
        ),
        migrations.RemoveField(
            model_name='interview',
            name='relevant_skills',
        ),
        migrations.AddField(
            model_name='interview',
            name='assertiveness',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='interview',
            name='communication',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='interview',
            name='education',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='interview',
            name='general_knowledge',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='interview',
            name='job_knowledge',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='interview',
            name='personality',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='interview',
            name='potential',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='interview',
            name='work_experience',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
