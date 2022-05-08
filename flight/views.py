from typing import Any, Dict

from django.http import HttpResponseNotAllowed
from django.shortcuts import render
from django.views.generic.base import TemplateView, View
from django.http.request import HttpRequest



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
