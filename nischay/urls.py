from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/bot/', include('bot.urls')),
    path('api/fortune/', include('fortune_wheel.urls')),
    path('api/eccomerce/', include('eccomerce.urls')),
    path('api/roi/', include('roi.urls')),
]
