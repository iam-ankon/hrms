# Generated by Django 5.1.6 on 2025-05-26 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchandiser', '0007_remove_inquiry_color_alter_colorsizegroup_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='year',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Year',
        ),
    ]
