# Generated by Django 3.2.7 on 2021-09-26 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phyApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='simulation_project',
            name='image',
        ),
    ]