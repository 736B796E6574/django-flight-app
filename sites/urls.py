from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sites', views.SiteList.as_view(), name='sites'),
]