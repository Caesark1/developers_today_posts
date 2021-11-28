from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from developers_today.swagger_scheme import schema_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("posts/", include("apps.posts.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
