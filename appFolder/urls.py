from . import views # views.py all
from rest_framework import routers
from django.urls import path

router = routers.DefaultRouter()
router.register('info', views.InfoView, 'info')
router.register('hospitalList', views.HospitalListView, 'hospitalList')
# router.register('',views.index,'index')
# router.register('infoForm',views.InfoFromView.as_view,'infoForm')
# router.register('provider',views.HopistalListView.as_view,'provider')

# urlpatterns = router.urls

urlpatterns = [
    # path('',views.index,name='index'),   # path ( route, view, kwargs, name )
                                        # route : url address
                                        # view : view
                                        # kwargs : deliveried argments
                                        # name : route's name
    path('hospital/all',views.HospitalList.as_view(),name='HospitalList'),
    path('hospitalDetail/<str:state>/',views.HospitalStateDetail.as_view(),name='HospitalStateDetail'),
    path('hospitalDetail/zipcode/<int:code>/',views.HospitalZipcodeDetail.as_view(),name='HospitalZipcodeDetail'),
    path('hospitalDetail/info/<int:hospital_id>/',views.HospitalDetail.as_view(),name='HospitalDetail'),
    path('info/register/',views.InfoTestPost.as_view()),
    path('getCSRF/',views.csrf),
    path('infoList',views.InfoList.as_view(),name='InfoList'),
    path('infoDetail',views.InfoDetail.as_view(),name='InfoDetail')
]