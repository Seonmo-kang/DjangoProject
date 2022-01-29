from django.urls import path, include
from . import views
from rest_framework import routers
# route = routers.DefaultRouter()
# route.register('info',views.InfoView,'info')
# route.register('index',views.index,'index')
# urlpatterns = route.urls

urlpatterns=[
    path('index/',views.index)

]