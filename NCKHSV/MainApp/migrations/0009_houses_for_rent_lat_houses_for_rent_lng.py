# Generated by Django 4.1.5 on 2023-04-17 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0008_alter_houses_for_rent_electric_water_heater'),
    ]

    operations = [
        migrations.AddField(
            model_name='houses_for_rent',
            name='lat',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='houses_for_rent',
            name='lng',
            field=models.CharField(max_length=255, null=True),
        ),
    ]