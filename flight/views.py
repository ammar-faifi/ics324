from array import array
import imp
from operator import mod
from typing import Any, Dict

from django.http import Http404, HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import redirect, render, resolve_url
from django.urls import reverse
from django.views.generic.base import TemplateView, View
from django.http.request import HttpRequest
from django.core.exceptions import ObjectDoesNotExist

from . import models
from data import cities

import flight



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
        data = request.POST
        data = {
            'date': data.get('date'),
            'source_city': data.get('source_city'),
            'destination': data.get('dest_city'),
        }

        flights = models.Flight.objects.filter(**data)
        print(flights)

        result = []
        for f in flights:
            result.append([f, {}])
            for c, _ in models.CLASSES:
                try:
                    total_seats = f.plane.model.class_info.filter(type=c)[0].total_seats
                    price = f.plane.model.class_info.filter(type=c)[0].price
                except:
                    total_seats = 0
                    price = None
                    
                result[-1][1][c] = total_seats - models.Ticket.objects.filter(class_type=c, flight=f).count()
                result[-1][1][c+'_price'] = price
        print(result)


        return render(
            request, 
            'flight/data-entry.html',
            context={
                'flights': flights, 
                'result': result,
                } | data
            )

class ManageBooking(View):

    def post(self, request:HttpRequest):
        try:
            booking_code = request.POST.get('booking_code')
            last_name = request.POST.get('last_name')
            ticket = models.Ticket.objects.get(code=booking_code, passenger__last_name=last_name)
        
        except ObjectDoesNotExist:
            return render(
                request,
                'flight/index.html',
                context={'message': 'We did not find your booking.'}
                )
        
        except Exception as e:
            return HttpResponse(e)

        return render(
            request,
            'flight/booking.html',
            context={'ticket': ticket}
        )


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


def book(request: HttpRequest):
    d = request.POST
    code, class_type = d.get('flight_selector').split('-')
    data = {
        'first_name': d.get('first-name'),
        'last_name': d.get('last-name'),
        'birth_date': d.get('birth-date'),
        'phone': d.get('phone'),
        'address': d.get('address'),
        'email': d.get('email'),
        'special_need': d.get('special-needs', False),
    }

    try:
        # create the Passenger object
        passenger = models.Passenger.objects.get_or_create(
            **data
        )

        # get the flight object chosen by user
        flight = models.Flight.objects.get(code=code)

        # create for the passenger its ticket
        ticket = models.Ticket.objects.create(
            code=models.get_random_unique_code(),
            seat_number = models.get_random_seat_code(flight),
            cost=flight.plane.model.class_info.get(type=class_type).price,
            class_type = class_type,
            gate='G10',
            passenger=passenger[0],
            flight=flight,
        )

    except Exception as e: 
        print(e)

    return render(
        request,
        'flight/booking_done.html',
        context={
            'ticket': ticket,
            'flight': flight,
        },
    )
