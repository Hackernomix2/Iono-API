from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view , permission_classes
from .models import User
from rest_framework.authtoken.models import Token
from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from rest_framework import status


@api_view(['POST'])
def sign_up(request):
    data = request.data.copy()
    serializer = UserSerializer(data=data)
    
    if serializer.is_valid():
        serializer.save()
        user = serializer.instance
        user.set_password(data['password'])
        token, created = Token.objects.get_or_create(user=user) # returns a tuple so 
        return Response({"user": serializer.data, "token": token.key}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_detail(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = User.objects.filter(username=username, password=password).first()
    
    if user:
        serialiser = UserSerializer(user)
        token, created = Token.objects.get_or_create(user=user) # returns a tuple so 
        return Response({"token": token.key , "user" : serialiser.data }, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    '''logout route'''

    Token.objects.filter(user=request.user).delete()
    return Response("successfully logged out", status=status.HTTP_200_OK)