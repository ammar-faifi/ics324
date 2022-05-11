from django.contrib import admin
from django.urls import path
from . import views

app_name = 'flight'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('search_flight', views.SearchFlight.as_view(), name='search_flight'),
    path('manage_booking', views.ManageBooking.as_view(), name='manage_booking'),
    path('get_cities', views.get_cities, name='get_cities'),
    path('book', views.book, name='book'),
]