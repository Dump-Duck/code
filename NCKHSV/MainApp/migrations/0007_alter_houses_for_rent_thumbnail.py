# Generated by Django 4.1.5 on 2023-03-28 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0006_houses_for_rent_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houses_for_rent',
            name='thumbnail',
            field=models.FileField(null=True, upload_to='MainApp/static/assets/img/house_photo/thumbnail'),
        ),
    ]