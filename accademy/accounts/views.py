

from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import RegisterSerializer
from rest_framework.permission import IsAuthenticated
from rest_framework.viewa import APIView
from rest_framework.response import Response

# Create your views here.


class RegisterView(CreateAPIView):
    Register_class = RegisterSerializer

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "email": request.user.email
        })
