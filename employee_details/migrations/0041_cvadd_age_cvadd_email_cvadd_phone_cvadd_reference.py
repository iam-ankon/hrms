# Generated by Django 5.1.6 on 2025-03-12 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_details', '0040_alter_terminationattachment_employee_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cvadd',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cvadd',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='cvadd',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='cvadd',
            name='reference',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
