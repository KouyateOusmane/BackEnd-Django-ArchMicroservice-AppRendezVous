from django.contrib import admin

# Register your models here.
from .models import Evaluation, Demande

admin.site.register( Evaluation)
admin.site.register( Demande)