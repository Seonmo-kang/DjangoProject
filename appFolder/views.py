from django.shortcuts import render
from django.http import HttpRequest, HttpResponse;

# Create your views here.
def index(request):
    return HttpResponse("Hello Django! This is Django project 1")