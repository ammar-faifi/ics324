from typing import Any, Dict
from django.shortcuts import render
from django.views.generic.base import TemplateView, View
from django.http.request import HttpRequest

# Create your views here.


class IndexView(TemplateView):

    template_name = "flight/index.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["test_var"] = "this a test var"
        return context


class CheckBooking(TemplateView):

    template_name = "flight/index.html"


    def get(self, request:HttpRequest):
        print(request.GET)
        return render(request, 'flight/booking.html')

    def post(self, request:HttpRequest):
        print(request.POST)
        return render(request, 'flight/booking.html')
