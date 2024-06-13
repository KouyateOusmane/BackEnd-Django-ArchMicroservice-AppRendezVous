# urls.py
from django.urls import path
from .views import ClientList, ClientCreate, ClientRetrieve, ClientUpdate, ClientDestroy
from .views import CustomTokenObtainPairView, TokenRefreshView
from .views import ClientList, ClientCreate, ClientRetrieve, ClientUpdate, ClientDestroy, MyTokenRefreshView


urlpatterns = [
    path('clients/', ClientList.as_view(), name='client-list'),
    path('clients/create/', ClientCreate.as_view(), name='client-create'),
    path('clients/<int:pk>/', ClientRetrieve.as_view(), name='client-retrieve'),
    path('clients/<int:pk>/update/', ClientUpdate.as_view(), name='client-update'),
    path('clients/<int:pk>/delete/', ClientDestroy.as_view(), name='client-destroy'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh')
]
