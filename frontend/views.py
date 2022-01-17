from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import InfoSerializer
from .models import InfoModel

# Create your views here.
def index(request):
    return render(request, 'frontend/index.html')
# class IndexView(viewsets.):
#     model =

class InfoView(viewsets.ModelViewSet):
    serializer_class = InfoSerializer
    queryset = InfoModel.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]