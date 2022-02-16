from django.shortcuts import render
from django.views.generic.base import TemplateView


class ReactView(TemplateView):
    template_name = 'frontend/index.html'
    def get_context_data(self, **kwargs):
        return {'context_variable': 'value'}
