# Generated by Django 4.2.1 on 2023-06-01 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0013_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='replys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.comments')),
            ],
        ),
    ]