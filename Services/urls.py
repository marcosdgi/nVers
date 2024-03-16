from django.urls import path
from Services.views.ServiceAPIView import ServiceAPIView

urlpatterns = [
    path('list_services/', ServiceAPIView.as_view(), name='list_services'),
    path('modify_services/', ServiceAPIView.as_view(), name='modify_services')
]
