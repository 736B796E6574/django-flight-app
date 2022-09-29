from django.contrib import admin
from .models import FlyingSite
from .models import Comment

admin.site.register(FlyingSite)
admin.site.register(Comment)

