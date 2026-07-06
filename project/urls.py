"""
URL configuration.

Add application routes here, e.g. `path('', include('apps.accounts.urls'))`.
See https://docs.djangoproject.com/en/6.0/topics/http/urls/
"""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(f'{settings.ADMIN_URL}/', admin.site.urls),
]

# Django Debug Toolbar (development only; the package is a dev dependency).
if settings.DEBUG:  # pragma: no cover
    urlpatterns += [path('__debug__/', include('debug_toolbar.urls'))]
