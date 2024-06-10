# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('prestataires/', views.PrestataireListCreate.as_view(), name='prestataire-list-create'),
    path('prestataires/<int:pk>/', views.PrestataireRetrieveUpdateDestroy.as_view(), name='prestataire-retrieve-update-destroy'),
]
