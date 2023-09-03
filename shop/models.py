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


class Products(models.Model):
    pID = models.CharField(max_length=20, primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    quantity = models.IntegerField()
    buying = models.IntegerField()
    # sell = models.IntegerField()
    discp = models.TextField(null=True)
    manufacturer = models.CharField(max_length=200)
    date = models.DateField(default=datetime.datetime.now())


class Orders(models.Model):
    orderID = models.CharField(max_length=20, primary_key=True, unique=True)
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.datetime.now())


class OrderList(models.Model):
    orderID = models.ForeignKey(Orders, on_delete=models.CASCADE)
    pID = models.ForeignKey(Products, on_delete=models.CASCADE)


class CancelOrder(models.Model):
    orderID = models.ForeignKey(Orders, on_delete=models.CASCADE)
    clsResn = models.TextField(null=False)


class Sell(models.Model):
    orderID = models.ForeignKey(Orders, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateField(default=datetime.date.today())

# class LastPurchase(models.Model):
#     pID = models.ForeignKey(Products, on_delete=models.CASCADE)
#     date = models.DateField(default=datetime.datetime.now())
#     buying = models.IntegerField()
#     quantity = models.IntegerField()
