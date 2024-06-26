from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include("apps.user.urls")),
    path('surface/detection/', include("apps.surface.urls")),
    path('flight/', include("apps.flight.urls")),
    path('wire/detection/', include("apps.wire.urls")),
    path('analytics/', include("apps.analytics.urls")),
    path('', include("apps.dashboard.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
