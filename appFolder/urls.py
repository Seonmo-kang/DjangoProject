from . import views # views.py all
from rest_framework import routers

router = routers.DefaultRouter()
router.register('info',views.InfoView,'info')
# router.register('',views.index,'index')
# router.register('infoForm',views.InfoFromView.as_view,'infoForm')
# router.register('provider',views.HopistalListView.as_view,'provider')

urlpatterns = router.urls

# urlpatterns = [
#     path('',views.index,name='index'),   # path ( route, view, kwargs, name )
#                                         # route : url address
#                                         # view : view
#                                         # kwargs : deliveried argments
#                                         # name : route's name
#     path('infoForm',views.InfoFromView.as_view(),name="infoForm"), # class based View must have .as_view() method in url
#     path('provider',views.HopistalListView.as_view(),name="provider")
# ]