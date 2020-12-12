from rest_framework import serializers

class LoginSerialzier(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class RegisterSerialzier(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField()
    password = serializers.CharField()
