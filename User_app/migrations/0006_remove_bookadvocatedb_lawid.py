# Generated by Django 4.1 on 2022-10-05 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User_app', '0005_rename_boodadvocate_bookadvocatedb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookadvocatedb',
            name='lawid',
        ),
    ]
