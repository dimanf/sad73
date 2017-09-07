from django.contrib import admin
from qa.models import qamodel

class qamodelAdmin(admin.ModelAdmin):
    """docstring for qamodelAdmin"""
    list_display = ('id', 'name', 'text', 'email', 'date_create', 'status')
    list_display_links = 'name',
    search_fields = ('name', 'text', 'email', 'date_create', 'status')



admin.site.register(qamodel, qamodelAdmin)	

	
		