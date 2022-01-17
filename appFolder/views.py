from django.http import HttpResponse;
from django.views.generic import ListView  # Display templates

from rest_framework import viewsets,permissions

from .models import Info, Hospital
from .serializers import InfoSerializer


class InfoView(viewsets.ModelViewSet):
    serializer_class = InfoSerializer
    queryset = Info.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

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