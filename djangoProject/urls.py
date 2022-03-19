from django.contrib import admin
from django.db import router
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from core.views import render_home, render_form, ObrashenieViewSet
from djangoProject import settings
router = DefaultRouter()
router.register(r'obrashenie', ObrashenieViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', render_form, name='render_add'),
    path('', render_home
         ),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)