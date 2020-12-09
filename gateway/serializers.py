from rest_framework import serializers

class LoginSerialzier(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()