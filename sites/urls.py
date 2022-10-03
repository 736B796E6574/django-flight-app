from django.urls import path
from . import views

urlpatterns = [
    path('', views.SiteList.as_view(), name='home'),
]