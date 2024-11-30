from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import RegistrationSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
# Create your views here.

class CustomerRegistrationView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "user_id": user.id,
                "username": user.username,
                "email": user.email,
                "token": token.key,
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        
        # Kullanıcıyı doğrulama
        user = authenticate(username=username, password=password)
        
        if user is not None:
            # Kullanıcı bulunduysa token oluştur
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "user_id": user.id,
                "username": user.username,
                "email": user.email,
                "token": token.key
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)
