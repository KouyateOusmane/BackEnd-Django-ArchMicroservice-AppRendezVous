from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import generics
from .models import Client
from .serializers import ClientSerializer

class ClientListCreate(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
