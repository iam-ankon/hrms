# Generated by Django 5.1.6 on 2025-03-04 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_details', '0015_alter_financeprovision_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvmanagement',
            name='letter_file',
            field=models.FileField(upload_to='cv_letters/'),
        ),
        migrations.AlterField(
            model_name='cvmanagement',
            name='letter_type',
            field=models.CharField(choices=[('offer_letter', 'Offer Letter'), ('appointment_letter', 'Appointment Letter'), ('joining_report', 'Joining Report')], max_length=50),
        ),
    ]
