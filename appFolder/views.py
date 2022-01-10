from django.shortcuts import render
from django.http import HttpRequest, HttpResponse;
from django.views.generic.base import TemplateView # Display templates
from django.views.generic import ListView  # Display templates

from .models import Info,Hospital


def index(request):
    return HttpResponse("Hello Django! This is Django project 1")
# def infoForm(request):
#     return HttpResponse("This is infoForm site ${0}".format(0))

# Using TemplateView : class based view, not function based view
class InfoFromView(ListView):
    # model = Info
    template_name = 'infoForm.html'

class HopistalListView(ListView):
    model = Hospital
    template_name = 'provider.html'
    # context_object_name = 'hospital_obj'  # context_object_name change
                                            # context_object_name : model object name