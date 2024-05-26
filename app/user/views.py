from django.shortcuts import render

# Create your views here.
"""
views for the user api
"""

from rest_framework import generics
from .serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""

    serializer_class = UserSerializer
