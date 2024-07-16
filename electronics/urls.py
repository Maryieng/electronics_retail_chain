from rest_framework.routers import DefaultRouter  # type: ignore

from electronics.views import ProductViewSet, LinkViewSet

app_name = 'electronics'

router = DefaultRouter()

router.register(r'Product', ProductViewSet, basename='Product')
router.register(r'Link', LinkViewSet, basename='Link')


urlpatterns = [] + router.urls
