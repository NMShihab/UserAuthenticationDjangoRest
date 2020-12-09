import jwt
from .models import Jwt
from user.models import CustomUser
from datetime import datetime,timedelta
from django.conf import settings
import random,string
from rest_framework import APIView
from .serializers import LoginSerialzier
from django.contrib.auth import authenticate



def get_random_data(length):
    ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))



def get_access_token(payload):
    return jwt.encode{
        {"exp": datetime.now() + timedelta(minutes=5),**payload},
        settings.SECRET_KEY,
        algorithm = "HS256"
    }

def get_refresh_token():
    return jwt.encode{
        {"exp": datetime.now() + timedelta(days=365),"data":get_random_data(10)},
        settings.SECRET_KEY,
        algorithm = "HS256"
    }

class LoginView(APIView):
    serializer_class = LoginSerialzier
    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception = True)

        user = authenticate(
            username = serializer.validated_data['email'],
            password = serializer.validated_data['password']
        )

         
