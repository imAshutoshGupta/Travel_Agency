# Generated by Django 4.2.7 on 2023-11-06 08:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_alter_booknow_d_journey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booknow',
            name='d_journey',
            field=models.DateField(default=datetime.date.today, verbose_name='Date of Journey'),
        ),
    ]
