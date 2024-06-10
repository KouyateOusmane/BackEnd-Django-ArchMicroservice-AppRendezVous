from django.contrib import admin

# Register your models here.
from .models import Demande, Prestataire, Client

admin.site.register(Demande)
admin.site.register(Prestataire)
admin.site.register(Client)