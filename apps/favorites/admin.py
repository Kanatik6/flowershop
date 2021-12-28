from django.contrib import admin

# Register your models here.
from apps.favorites.models import Favorite

admin.site.register(Favorite)
