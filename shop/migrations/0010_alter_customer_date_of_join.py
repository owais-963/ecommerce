# Generated by Django 4.2.4 on 2023-08-08 22:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_customer_date_of_join_customer_dob_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_of_join',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 3, 11, 4, 736445)),
        ),
    ]
