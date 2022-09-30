from django.contrib import admin
from .models import FlyingSite, Comment, Photos
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(Comment)
admin.site.register(Photos)

@admin.register(FlyingSite)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('overview')
    prepopulated_fields = {'slug': ('site_name',)}

