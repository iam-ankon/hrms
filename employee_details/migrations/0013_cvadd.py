# Generated by Django 5.1.6 on 2025-03-03 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_details', '0012_rename_name_notification_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='CVAdd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('cv_file', models.FileField(upload_to='cv_adds/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
