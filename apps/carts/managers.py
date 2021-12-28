from django.db import models
from apps.carts.models import *


class CartManager(models.Manager):
    def get_or_new(self, request):
        user = request.user
        cart_id = request.session.get('cart_id', None)
        if user is not None and user.is_authenticated:
            if user.cart:
                cart_obj = request.user.cart
            else:
                cart_obj = Cart.objects.get(pk=cart_id)
                cart_obj.user = user
                cart_obj.save()
            return cart_obj
        else:
            cart_obj = Cart.objects.get_or_create(pk=cart_id)
            cart_id = request.session['cart_id'] = cart_obj[0].id
            return cart_obj[0]