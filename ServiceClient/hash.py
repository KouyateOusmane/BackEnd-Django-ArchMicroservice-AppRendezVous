from django.contrib.auth.hashers import make_password
from .models import Client

# Mettre à jour les mots de passe pour les clients existants
clients = Client.objects.all()
for client in clients:
    client.password = make_password(client.password)
    client.save()