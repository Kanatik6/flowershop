from django.urls import path

from apps.carts.views import CartItemDetailView, CartDetailView, CartItemCreate

urlpatterns = [
    path("cartitem/create/", CartItemCreate.as_view(), name="cart-item-create"),
    path("cart/<int:pk>/", CartDetailView.as_view()),
    path("cartitem/<int:pk>/", CartItemDetailView.as_view()),
]
