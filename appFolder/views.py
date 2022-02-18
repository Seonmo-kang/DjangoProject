from django.http import HttpResponse, Http404;
from django.views.generic import ListView  # Display templates

from rest_framework import generics
from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework import viewsets,permissions
from rest_framework import status

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

<<<<<<< Updated upstream
# Using TemplateView : class based view, not function based view
class InfoFromView(ListView):
    # model = Info
    template_name = 'infoForm.html'

class HopistalListView(ListView):
    model = Hospital
    template_name = 'provider.html'
    # context_object_name = 'hospital_obj'  # context_object_name change
                                            # context_object_name : model object name
=======

"""
Using APIView - rewritting our class-based views
"""
class HospitalList(APIView):
    """
    List all Hospitals, or create a new Hospital
    """
    def get(self, request, format=None):
        hospital = Hospital.objects.all()
        serializer = HospitalListSerializer(hospital,many=True)
        return Response(serializer.data)
    def post(self,request,format=None):
        serializer = HospitalListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
"""
    /hospitalDetail/<int:hospital_id>/
"""
class HospitalDetail(APIView):
    """
    Retrieve, Update or delete a Hospital instance
    """
    def get_object(self,hospital_id):
        try:
            return Hospital.objects.get(hospital_id=hospital_id)
        except Hospital.DoesNotExist:
            return Http404

    def get(self,request,hospital_id,format=None):
        hospital = self.get_object(hospital_id)
        serializer = HospitalListSerializer(hospital)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        hospital = self.get_object(pk)
        serializer = HospitalListSerializer(hospital, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        hospital = self.get_object(pk)
        hospital.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""
    /hospitalDetail/<str:city>/
"""
class HospitalStateDetail(APIView):
    """
    Retrieve, Update or delete a Hospital instance
    """
    def get_object(self,city):
        try:
            return Hospital.objects.all().filter(hospital_city=city)
        except Hospital.DoesNotExist:
            return Http404

    def get(self,request,city,format=None):
        hospital = self.get_object(city)
        serializer = HospitalListSerializer(hospital,many=True)
        return Response(serializer.data)

# class HospitalDetail()


class InfoList(generics.ListCreateAPIView):
    queryset = Info.objects.all()
    serializer_class =  InfoSerializer
class InfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
>>>>>>> Stashed changes
