from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.bot_register),
    path('withdraw/', views.request_withdrawal),
    path('franchise/<int:user_id>/', views.check_franchise),
]
