from . import views # views.py all
from rest_framework import routers
from django.urls import path

router = routers.DefaultRouter()
<<<<<<< Updated upstream
router.register('info',views.InfoView,'info')
# router.register('',views.index,'index')
# router.register('infoForm',views.InfoFromView.as_view,'infoForm')
# router.register('provider',views.HopistalListView.as_view,'provider')
=======
router.register('info', views.InfoView, 'info')
router.register('hospitalList', views.HospitalListView, 'hospitalList')
# router.register('hospitalList',views.HospitalList,'HospitalList')
# router.register('hospitalDetail',views.HospitalDetail,'HospitalDetail')

# urlpatterns = router.urls
urlpatterns = [
#     # path('',views.index,name='index'),   # path ( route, view, kwargs, name )
#     # route : url address
#     # view : view
#     # kwargs : deliveried argments
#     # name : route's name
    path('hospital/all',views.HospitalList.as_view(),name='HospitalList'),
    path('hospitalDetail/<int:hospital_id>/',views.HospitalDetail.as_view(),name='HospitalDetail'),
    path('hospitalDetail/<str:city>/',views.HospitalStateDetail.as_view(),name='HospitalStateDetail'),
    path('infoList',views.InfoList.as_view(),name='InfoList'),
    path('infoDetail',views.InfoDetail.as_view(),name='InfoDetail')
]

>>>>>>> Stashed changes


