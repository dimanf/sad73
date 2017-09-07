from django.conf.urls import patterns, include, url
from qa.views import qa
from gallery.views import gallery
from gallery.views import gallery_request
from ourgroups.views import our_groups
from ourgroups.views import work_with_us
from ourgroups.views import work_with_us_group
from ourgroups.views import day_regimen
from ourgroups.views import setka_zan
from ourgroups.views import live_our_group
from ourgroups.views import sovet_group_educator

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^question-answer/$', qa),
    (r'^photos/$', gallery),
    (r'^photos/(\d+)/$', gallery_request),
    (r'^our-grups/$', our_groups),
    (r'^our-grups/(\d+)/$', work_with_us),
    (r'^our-grups/work-with-us/(\d+)/$', work_with_us_group),
    (r'^our-grups/day-regimen/(\d+)/$', day_regimen),
    (r'^our-grups/setka-zanyatiy/(\d+)/$', setka_zan),
    (r'^our-grups/live-our-grups/(\d+)/$', live_our_group),
    (r'^our-grups/sovet-educator/(\d+)/$', sovet_group_educator),
    (r'^admin/filebrowser/', include('filebrowser.urls')),
    (r'^tinymce/', include('tinymce.urls')),

    # Examples:
    # url(r'^$', 'tg.views.home', name='home'),
    # url(r'^tg/', include('tg.foo.urls')),
        
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
