from django.contrib import admin
from .models import FlyingSite, Comment, Photo
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('site_name',)}
    actions = ['approve_photos']
    list_display = ('site_name', 'updated_on', 'approved')
    search_fields = ['site_name', 'wind_direction']
    list_filter = ('approved', 'updated_on')
    
    def approve_photos(self, request, queryset):
        queryset.update(approved=True)




@admin.register(FlyingSite)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('site_name',)}
    actions = ['approve_sites']
    list_display = ('site_name', 'updated_on', 'approved')
    search_fields = ['site_name', 'wind_direction']
    list_filter = ('approved', 'updated_on')

    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

