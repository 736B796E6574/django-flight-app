from django.views import generic 
from django.shortcuts import render
from django.http import HttpResponse
from .models import FlyingSite

class SiteList(generic.ListView):
    model = FlyingSite
    queryset = FlyingSite.objects.filter(status=1).order_by('-updated_on')
    template_name = 'flying_sites.html'
    paginate_by = 8


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
