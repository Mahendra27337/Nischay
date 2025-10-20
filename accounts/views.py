from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import PasswordResetOTP

class RegisterAPIView(APIView):
    def post(self, request):
        s = RegisterSerializer(data=request.data)
        if s.is_valid():
            user = s.save()
            return Response({'message':'registered','username':user.username}, status=201)
        return Response(s.errors, status=400)

class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({'access':str(refresh.access_token),'refresh':str(refresh)})
        return Response({'error':'invalid credentials'}, status=401)

class RequestOtpAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        user = User.objects.filter(username=username).first()
        if not user: return Response({'error':'user not found'}, status=404)
        otp = PasswordResetOTP.generate_otp()
        PasswordResetOTP.objects.create(user=user, otp=otp)
        # for testing, return otp in response (in prod send via SMS/email)
        return Response({'message':'otp generated','otp':otp})

class VerifyOtpResetAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        otp = request.data.get('otp')
        new_password = request.data.get('new_password')
        user = User.objects.filter(username=username).first()
        if not user: return Response({'error':'user not found'}, status=404)
        rec = PasswordResetOTP.objects.filter(user=user, otp=otp).order_by('-created_at').first()
        if not rec: return Response({'error':'invalid otp'}, status=400)
        user.set_password(new_password); user.save()
        rec.delete()
        return Response({'message':'password reset successful'})
