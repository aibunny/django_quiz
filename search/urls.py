from django.urls import path
from .views import search_passengers


app_name = 'search'

urlpatterns = [
    path('passengers/', search_passengers, name='search'),
]