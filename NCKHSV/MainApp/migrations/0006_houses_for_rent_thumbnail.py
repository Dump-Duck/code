# Generated by Django 4.1.5 on 2023-03-28 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0005_houses_for_rent_electric_water_heater'),
    ]

    operations = [
        migrations.AddField(
            model_name='houses_for_rent',
            name='thumbnail',
            field=models.FileField(null=True, upload_to='MainApp/static/assets/img/thumbnail'),
        ),
    ]