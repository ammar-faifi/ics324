from typing import Any, Dict
from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.


class IndexView(TemplateView):

    template_name = "flight/index.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["test_var"] = "this a test var"
        return context


def check_booking(request):
    print(request)
    print(request.DATA)
    return
