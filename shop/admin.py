from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(Products)
admin.site.register(Sell)
admin.site.register(Orders)
admin.site.register(OrderList)
admin.site.register(CancelOrder)