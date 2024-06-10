from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import generics
from .models import Prestataire
from .serializers import PrestataireSerializer

class PrestataireListCreate(generics.ListCreateAPIView):
    queryset = Prestataire.objects.all()
    serializer_class = PrestataireSerializer

class PrestataireRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prestataire.objects.all()
    serializer_class = PrestataireSerializer