from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ('username','email','password','password2')
        extra_kwargs = {'password': {'write_only': True}}
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Passwords do not match')
        return data
    def create(self, validated):
        u = User.objects.create_user(username=validated['username'], email=validated.get('email',''))
        u.set_password(validated['password'])
        u.save()
        return u
