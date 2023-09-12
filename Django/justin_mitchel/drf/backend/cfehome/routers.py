from rest_framework.routers import DefaultRouter
from products_10.viewsets import ProductViewSet, ProductGenericViewSet

router = DefaultRouter()
router.register('products-viewset', ProductViewSet, basename='api_06_products_10_viewsets')
router.register('products-generic-viewset', ProductGenericViewSet, basename='api_06_products_10_generic_viewsets')


urlpatterns = router.urls