# Generated by Django 4.2.4 on 2023-08-08 21:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_remove_customer_date_of_join'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='dob',
        ),
        migrations.AddField(
            model_name='customer',
            name='date_of_join',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 2, 49, 37, 550333)),
        ),
    ]