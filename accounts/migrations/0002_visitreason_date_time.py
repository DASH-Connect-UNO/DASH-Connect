# Generated by Django 4.1.7 on 2024-08-10 16:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitreason',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
