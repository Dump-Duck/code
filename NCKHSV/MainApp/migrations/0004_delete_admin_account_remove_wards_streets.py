# Generated by Django 4.1.5 on 2023-02-21 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_districts_wards_provinces_districts_wards_streets'),
    ]

    operations = [
        migrations.DeleteModel(
            name='admin_account',
        ),
        migrations.RemoveField(
            model_name='wards',
            name='streets',
        ),
    ]