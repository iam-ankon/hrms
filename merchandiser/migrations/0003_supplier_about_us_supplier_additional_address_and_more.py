# Generated by Django 5.1.6 on 2025-04-17 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchandiser', '0002_buyer_customer_remarks_customer_buyer'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='about_us',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='additional_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='bank_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='capability',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='contect_mobile',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='contect_person',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='contract_sign_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='country_region',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='deactivation_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='deactivation_reason',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='eu_country',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='gps_lat',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='gps_lng',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='holding_group',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='local_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='migrated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='supplier',
            name='name_1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='name_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='name_3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='number_of_running_factories',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='place_of_incorporation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='planned_inactivation_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='postal_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='preferred_language',
            field=models.CharField(blank=True, default='English', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='purchasing_group',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='reason_for_enlistment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='reference_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='short_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='swift_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='town_city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='vendor_access_creation',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='vendor_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='vendor_rating',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='vendor_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='year_established',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='wgr',
            field=models.IntegerField(blank=True, null=True, verbose_name='W.G.R'),
        ),
    ]
