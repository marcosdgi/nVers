from django.urls import path

from Projects.views.ProjectAPIView import ProjectAPIView

urlpatterns = [
    path('list_projects/', ProjectAPIView.as_view(), name='list_projects'),
    path('modify_project/<int:pk>', ProjectAPIView.as_view(), name='modify_project')
]
{}