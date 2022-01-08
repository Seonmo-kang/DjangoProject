from django.shortcuts import render
from django.http import HttpRequest, HttpResponse;
from django.views.generic.base import TemplateView # Display templates

# Create your views here.
def index(request):
    return HttpResponse("Hello Django! This is Django project 1")
# def infoForm(request):
#     return HttpResponse("This is infoForm site ${0}".format(0))

# Using TemplateView : class based view, not function based view
class InfoFromView(TemplateView):
    template_name = 'infoForm.html'

class HopistalListView(TemplateView):
    template_name = 'provider.html'