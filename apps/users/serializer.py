from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as SimpleTokenObtainPairSerializer,
)

from apps.favorites.models import Favorite
from apps.users.models import User


class TokenObtainPairSerializer(SimpleTokenObtainPairSerializer):
    default_error_messages = {
        "no_active_account": _(
            "Активная учетная запись с указанными учетными данными не найдена"
        )
    }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "is_active",
            "password",
        )
        read_only_fields = ("id",)

    def update(self, instance, validated_data):
        instance.email = validated_data.get("email", instance.email)
        instance.is_active = validated_data.get("is_active", True)
        instance.save()
        return instance


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255)
    password_repeat = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "password",
            "password_repeat",
        )

    def create(self, validated_data):
        password = validated_data["password"]
        password_repeat = validated_data["password_repeat"]
        if password == password_repeat:
            user = User.objects.create(
                email=validated_data["email"],
            )
            user.set_password(password)
            user.is_active = True
            user.save()
            fav = Favorite.objects.create(user=user)
            fav.save()
            return user
        raise serializers.ValidationError({"password": "Ваши пароли не совпадают."})
