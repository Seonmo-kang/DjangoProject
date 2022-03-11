from django.http import HttpResponse, Http404, JsonResponse;
# for CSRF
from django.middleware.csrf import get_token
from rest_framework.request import Request
from rest_framework import generics
from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets,permissions

from .models import Info, Hospital
from .serializers import InfoSerializer, HospitalListSerializer

# return csrf json file
def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})

class InfoPost(APIView):
    def post(self,request,format=None):
        serializer = InfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class InfoTestPost(APIView):
    def post(self,request,format=None):
        print("requested data is "+str(request.data['values']))
        customer_data = request.data['values']
        hospital_id = Hospital.objects.get(hospital_id=customer_data["hospital"])
        # info = Info(info_firstName = customer_data["firstName"],
        #             info_lastName = customer_data["lastName"],
        #             info_dateOfBirth = customer_data["birthOfDate"],
        #             info_state = customer_data["state"],
        #             info_zipCode = customer_data["zipcode"],
        #             info_vaccine = customer_data["vaccine"],
        #             info_vaccineType = customer_data["vaccineType"],
        #             info_consentAck = customer_data["consentAck"],
        #             info_hospital_id = Hospital.objects.get(hospital_id=customer_data["hospital"]) # *Foreign key
        #             )
        infoSerializer = InfoSerializer.create(Info,validated_data={"info_firstName" : customer_data["firstName"],
                                                           "info_lastName" : customer_data["lastName"],
                                                           "info_dateOfBirth" : customer_data["birthOfDate"],
                                                           "info_state" : customer_data["state"],
                                                           "info_zipCode" : customer_data["zipcode"],
                                                           "info_vaccine" : customer_data["vaccine"],
                                                           "info_vaccineType" : customer_data["vaccineType"],
                                                           "info_consentAck" : customer_data["consentAck"],
                                                           "info_hospital_id" : hospital_id})
        if(infoSerializer):
            return Response({"request":"ok"},status=status.HTTP_201_CREATED)
        else:
            return  Response(infoSerializer.data,status=status.HTTP_400_BAD_REQUEST)

class InfoView(viewsets.ModelViewSet):
    serializer_class = InfoSerializer
    queryset = Info.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

class HospitalListView(viewsets.ModelViewSet):
    serializer_class = HospitalListSerializer
    queryset = Hospital.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    # context_object_name = 'hospital_obj'  # context_object_name change
    # context_object_name : model object name

# def index(request):
#     return HttpResponse("Hello Django! This is Django project 1")
# # def infoForm(request):
# #     return HttpResponse("This is infoForm site ${0}".format(0))
#
# # Using TemplateView : class based view, not function based view
# class InfoFromView(ListView):
#     # model = Info
#     template_name = 'infoForm.html'

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
    def get_object(self,state):
        try:
            return Hospital.objects.all().filter(hospital_state=state)
        except Hospital.DoesNotExist:
            return Http404

    def get(self,request,state,format=None):
        hospital = self.get_object(state)
        serializer = HospitalListSerializer(hospital,many=True)
        return Response(serializer.data)

"""
    /hospitalDetail/<int:code>/
"""
class HospitalZipcodeDetail(APIView):
    """
    Retrieve, Update or delete a Hospital instance
    """
    def get_object(self,code):
        try:
            return Hospital.objects.all().filter(hospital_zipcode=code)
        except Hospital.DoesNotExist:
            return Http404

    def get(self,request,code,format=None):
        hospital = self.get_object(code)
        serializer = HospitalListSerializer(hospital,many=True)
        return Response(serializer.data)

# class HospitalDetail()
class InfoList(generics.ListCreateAPIView):
    queryset = Info.objects.all()
    serializer_class =  InfoSerializer

class InfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
