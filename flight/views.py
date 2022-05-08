from array import array
from typing import Any, Dict

from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView, View
from django.http.request import HttpRequest
from . import models



class IndexView(TemplateView):

    template_name = "flight/index.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context


class SearchFlight(View):

    http_method_names = View.http_method_names.copy()
    http_method_names.remove('get')


    def post(self, request:HttpRequest):
        print(request.POST)
        return render(request, 'flight/booking.html')


def get_cities(request: HttpRequest):
    source = request.POST.get('source_city')
    arrival_cities = models.Flight.objects.filter(source_city=source).values_list('destination', flat=True)
    return JsonResponse(list(arrival_cities))