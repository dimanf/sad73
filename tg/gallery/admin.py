# -*- coding: utf-8 -*-
from django.contrib import admin

from gallery.models import Gallery, Image

class GalleryAdmin(admin.ModelAdmin):
    """Класс админки для категорий"""    
    list_display = ('name', 'date_create')
    list_display_links = ('name',)
    search_fields = ('name', 'date_create')

admin.site.register(Gallery, GalleryAdmin)    
admin.site.register(Image)