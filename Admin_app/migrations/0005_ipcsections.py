# Generated by Django 4.1 on 2022-10-14 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_app', '0004_law'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPCSections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipcsection', models.CharField(max_length=20)),
                ('ipcdescription', models.CharField(max_length=100)),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin_app.law')),
            ],
        ),
    ]
