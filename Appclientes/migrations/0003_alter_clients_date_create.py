# Generated by Django 4.0.4 on 2022-06-26 16:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appclientes', '0002_rename_client_clients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='date_create',
            field=models.DateTimeField(verbose_name=datetime.date),
        ),
    ]