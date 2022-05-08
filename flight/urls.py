from django.contrib import admin
from django.urls import path
from . import views

app_name = 'flight'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('search_flight', views.SearchFlight.as_view(), name='search_flight')
]