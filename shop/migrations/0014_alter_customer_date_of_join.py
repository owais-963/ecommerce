# Generated by Django 4.2.4 on 2023-08-23 10:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_customer_password_alter_customer_date_of_join'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_of_join',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 23, 15, 48, 36, 443152)),
        ),
    ]