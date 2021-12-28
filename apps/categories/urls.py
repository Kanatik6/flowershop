from rest_framework.routers import DefaultRouter

from apps.categories.views import CategoryView

router = DefaultRouter()
router.register("", CategoryView, basename="category")

urlpatterns = router.urls
