# Generated by Django 4.0 on 2024-03-05 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bngjob',
            name='phonenumber',
        ),
        migrations.RemoveField(
            model_name='hydjob',
            name='phonenumber',
        ),
        migrations.RemoveField(
            model_name='punjob',
            name='phonenumber',
        ),
    ]
