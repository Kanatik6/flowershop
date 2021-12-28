from rest_framework_simplejwt.views import (
    TokenObtainPairView as SimpleTokenObtainPairView,
)
from rest_framework import viewsets
from apps.users.serializer import *
from apps.users.models import User
from rest_framework.generics import CreateAPIView


class TokenObtainPairView(SimpleTokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action in ["create"]:
            return UserCreateSerializer
        return self.serializer_class


class UserRegistartions(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    



