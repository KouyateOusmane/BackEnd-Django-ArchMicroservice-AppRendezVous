from django.shortcuts import render


from rest_framework import generics
from .models import Client
from .serializers import ClientSerializer

# views.py
class ClientList(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientCreate(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientRetrieve(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientUpdate(generics.UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientDestroy(generics.DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
