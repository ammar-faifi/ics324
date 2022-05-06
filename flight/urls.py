from django.contrib import admin
from django.urls import path
from . import views

app_name = 'flight'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('check_booking', views.CheckBooking.as_view(), name='check_booking')
]