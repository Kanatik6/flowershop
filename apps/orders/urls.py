from django.urls import path
from .views import *
from .models import *
from apps.orders import views


urlpatterns = [
    path("", views.OrderListCreateView.as_view()),
    path("<int:pk>/", views.OrderDetailView.as_view()),
]
