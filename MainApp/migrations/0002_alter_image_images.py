# Generated by Django 4.1.5 on 2023-02-22 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='images',
            field=models.FileField(upload_to='C:\\Users\\nguye\\Downloads\\Code\\code\\NCKHSV\\MainApp\\static\\assets\\img\\house_photo'),
        ),
    ]
