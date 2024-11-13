from django.shortcuts import render
from rest_framework import generics
from .models import CustomUser
from .serializers import CustomUserSerializer

class UserListView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


