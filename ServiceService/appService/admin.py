from django.contrib import admin

# Register your models here.
from .models import Service, Prestataire

admin.site.register(Service)
admin.site.register(Prestataire)