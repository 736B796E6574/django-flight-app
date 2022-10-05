from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sites/', views.SiteList.as_view(), name='sites'),
    path('gallery/', views.PhotoList.as_view(), name='gallery'),
    path('contact/', views.Contact, name='contact'),
]