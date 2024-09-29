from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),  # подключаем маршруты приложения myapp
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)