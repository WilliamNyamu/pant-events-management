from django.shortcuts import render
from .serializers import RegisterSerializer, ProfileSerializer
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authentication import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .permissions import IsUserorReadOnly


# Create your views here.

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        raise ValueError("Enter all the fields")
    
    user = authenticate(email = email, password = password)

    if user:
        # get their token
        token = Token.objects.get(user = user)
        return Response(
            {
                'token': token.key,
                'user_id': user.id,
                'email': user.email,
                'message': 'Login successful'
            },
            status=status.HTTP_200_OK
        )
    else:
        return Response(
            {
                'error': 'User not found'
            },
            status=status.HTTP_404_NOT_FOUND
        )
    

class ProfileListView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # return the profile for the currently authenticated user
        queryset = User.objects.filter(id = self.request.user.id)
        return queryset

class ProfileUpdateView(generics.UpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsUserorReadOnly]

    def get_queryset(self):
        queryset = User.objects.filter(id = self.request.user.id)
        return queryset
    

