from django.urls import path
from .views import RegisterAPIView, LoginAPIView, RequestOtpAPIView, VerifyOtpResetAPIView
urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('password-reset/request/', RequestOtpAPIView.as_view()),
    path('password-reset/verify/', VerifyOtpResetAPIView.as_view()),
]
