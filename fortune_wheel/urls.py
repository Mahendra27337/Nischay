from django.urls import path
from .views import PayPerSpinAPIView, DailySpinAPIView
urlpatterns = [
    path('pay-per-spin/', PayPerSpinAPIView.as_view()),
    path('daily-spin/', DailySpinAPIView.as_view()),
]
