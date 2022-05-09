from array import array
from operator import mod
from typing import Any, Dict
from django import views

from django.http import Http404, HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import redirect, render, resolve_url
from django.views.generic.base import TemplateView, View
from django.http.request import HttpRequest
from . import models
from data import cities



class IndexView(TemplateView):

    template_name = "flight/index.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['cities'] = cities
        return context


class SearchFlight(View):

    http_method_names = View.http_method_names.copy()
    http_method_names.remove('get')


    def post(self, request:HttpRequest):
        print(request.POST)
        return render(request, 'flight/booking.html')

class ManageBooking(View):

    def post(self, request:HttpRequest):
        try:
            booking_code = request.POST.get('booking_code')
            last_name = request.POST.get('last_name')

            ticket = models.Flight.objects.get(pk=booking_code, passenger__last_name=last_name)
        except:
            return Http404(request)
        print(ticket)
        return redirect('flight:index')


def get_cities(request: HttpRequest):
    source = request.POST.get('source_city', '')
    arrival = request.POST.get('dest_city', '')

    cities_list = []
    if source:
        arrival_cities = models.Flight.objects.filter(source_city=source).only('destination')
        for q in arrival_cities:
            cities_list.append({'code': q.destination, 'city': q.get_destination_display()})
        return JsonResponse(cities_list, safe=False)
    
    elif arrival:
        soure_cities = models.Flight.objects.filter(destination=source).values_list('source_city', flat=True)
        for q in soure_cities:
            cities_list.append({'code': q.source_city, 'city': q.get_source_city_display()})
        return JsonResponse(cities_list, safe=False)
    
    else:
        for city in cities:
            cities_list.append({'code': city[0], 'city': city[1]})
        return JsonResponse(cities_list, safe=False)