from django.urls import path
from .views import PlansAPIView, InvestAPIView
urlpatterns = [
    path('plans/', PlansAPIView.as_view()),
    path('invest/', InvestAPIView.as_view()),
]
