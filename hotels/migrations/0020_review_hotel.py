# Generated by Django 5.1.3 on 2025-01-01 09:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0019_rename_district_name_hotel_district_names'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='hotel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hotels.hotel'),
        ),
    ]