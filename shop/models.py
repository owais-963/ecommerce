import datetime

from django.db import models


# Create your models here.
class Customer(models.Model):
    Fname = models.CharField(max_length=50, null=False)
    Lname = models.CharField(max_length=50, null=True, blank=True)
    NICno = models.IntegerField(primary_key=True, unique=True)
    email = models.EmailField(null=True, blank=True)
    phoneNo = models.CharField(max_length=15, null=False)
    password = models.CharField(max_length=50, null=False, blank=False)
    dob = models.DateField(auto_now=False, null=True, blank=True)
    date_of_join = models.DateTimeField(default=datetime.datetime.now())


class Address(models.Model):
    customer_ID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    postal_code = models.IntegerField()
    street_add = models.CharField(max_length=200)
