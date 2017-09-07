# -*- coding: utf-8 -*-
from django.contrib import admin

from ourgroups.models import (Groups, WorkWithUs, Group,
                                ModeDay, SetkaZan, LiveOurGroups, SovetEducator)

class GroupsAdmin(admin.ModelAdmin):
    """Класс админки для групп"""    
    list_display = ('name', 'image','date_create',)
    list_display_links = ('name',)
    search_fields = ('name', 'date_create',)

class WorkWithUsAdmin(admin.ModelAdmin):
    """Класс админки для Работают с нами"""
    list_display = ('group', 'text', )
    list_display_links = ('group',)
    search_fields = ('group', 'text',)

class GroupAdmin(admin.ModelAdmin):
    """docstring for WorkWithUs_Work"""
    list_display = ('group', 'text', )
    list_display_links = ('group',)
    search_fields = ('group', 'text',)

class ModeDayAdmin(admin.ModelAdmin):
    list_display = ('group', 'text', )
    list_display_links = ('group',)
    search_fields = ('group', 'text',)

class SetkaZanAdmin(admin.ModelAdmin):
    list_display = ('group', 'text', )
    list_display_links = ('group',)
    search_fields = ('group', 'text',)

class LiveOurGroupsAdmin(admin.ModelAdmin):
    list_display = ('group', 'text', )
    list_display_links = ('group',)
    search_fields = ('group', 'text',)  

class SovetEducatorAdmin(admin.ModelAdmin):
    list_display = ('group', 'text', )
    list_display_links = ('group',)
    search_fields = ('group', 'text',)	 		    


admin.site.register(Groups, GroupsAdmin)    
admin.site.register(WorkWithUs, WorkWithUsAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(ModeDay, ModeDayAdmin)
admin.site.register(SetkaZan, SetkaZanAdmin)
admin.site.register(LiveOurGroups, LiveOurGroupsAdmin)
admin.site.register(SovetEducator, SovetEducatorAdmin)