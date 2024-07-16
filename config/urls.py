from django.contrib import admin   # type: ignore
from django.urls import path, include   # type: ignore
from drf_yasg import openapi   # type: ignore
from drf_yasg.views import get_schema_view   # type: ignore
from rest_framework import permissions   # type: ignore
from django.conf.urls.static import static   # type: ignore
from django.conf import settings   # type: ignore


schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('', include('electronics.urls', namespace='electronics')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
