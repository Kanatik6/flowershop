from rest_framework.routers import DefaultRouter

from apps.favorites.views import FavoriteViewSet
from apps.products.views import ProductAPIViewSet, ProductImageAPIViewSet

router = DefaultRouter()
router.register("", FavoriteViewSet, basename="favorites")

urlpatterns = router.urls
