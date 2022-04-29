from django.shortcuts import render
from django.views.generic.base import TemplateView


class IndexView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['test_var'] = 'this a test var'
        return context