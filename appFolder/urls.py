from django.urls import path
from . import views # views.py all

urlpatterns = [
    path('',views.index,name='index'),   # path ( route, view, kwargs, name )
                                        # route : url address
                                        # view : view
                                        # kwargs : deliveried argments
                                        # name : route's name
    path('infoForm',views.InfoFromView.as_view(),name="InfoForm"), # class based View must have .as_view() method in url
    path('provider',views.HopistalListView.as_view(),name="Provider")
]