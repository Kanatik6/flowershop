from django.contrib import admin
from apps.orders.models import Order, ProductOrder
admin.site.register(Order)
admin.site.register(ProductOrder)
