from django.contrib import admin
from .models import FlyingSite, Comment, Photos


admin.site.register(FlyingSite)
admin.site.register(Comment)
admin.site.register(Photos)

