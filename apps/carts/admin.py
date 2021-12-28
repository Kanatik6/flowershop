from django.contrib import admin

from apps.carts.models import CartItem, Cart

admin.site.register(CartItem)
admin.site.register(Cart)
