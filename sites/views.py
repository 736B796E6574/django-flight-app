import re
from django.views import generic, View
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import FlyingSite, Photo

class SiteList(generic.ListView):
    model = FlyingSite
    queryset = FlyingSite.objects.filter(status=1).order_by('-updated_on')
    template_name = 'flying_sites.html'
    paginate_by = 8

class SiteDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = FlyingSite.objects.filter(status=1)
        site = get_object_or_404(queryset, slug =slug)
        comments = site.discussion.filter(approved = True).order_by('created on')
        liked = False
        if site.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "site_detail.html",
            {
            "site":site,
            "comments": comments,
            "liked":liked,
            }
        )

def index(request):
    return render(
        request,
        "index.html",
    )

class PhotoList(generic.ListView):
    model = Photo
    queryset = Photo.objects.filter(status=1).order_by('-updated_on')
    template_name = 'gallery.html'
    paginate_by = 8

def Contact(request):
    return render(
        request,
        "contact.html",
    )
     