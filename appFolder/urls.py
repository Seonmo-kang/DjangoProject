from django.urls import path
from. import views

urlpatterns = [
    path('',views.index,name='index')   # path ( route, view, kwargs, name )
                                        # route : url address
                                        # view : view
                                        # kwargs : deliveried argments
                                        # name : route's name

]