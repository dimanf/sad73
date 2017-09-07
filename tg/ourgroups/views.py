# -*- coding: utf-8 -*-
import datetime

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

from ourgroups.models import (Groups, WorkWithUs, Group, ModeDay,
                                SetkaZan, LiveOurGroups, SovetEducator)

def our_groups(request):
	
    groups_list = Groups.objects.all()

    return render_to_response('our_groups.html', locals(),\
    context_instance = RequestContext(request))

def work_with_us(request, id):
    
    try:
        group = Group.objects.get(group_id = id)    
        work_wu = WorkWithUs.objects.get(group_id = id)
        mode_day = ModeDay.objects.get(group_id = id)
        setka = SetkaZan.objects.get(group_id = id)
        live_group = LiveOurGroups.objects.get(group_id = id)
        sovet_educator = SovetEducator.objects.get(group_id = id)
    except:
        raise Http404   
   

    return render_to_response('work_with_us.html', locals(),\
    context_instance = RequestContext(request))

def work_with_us_group(request, id):
	work_wu = WorkWithUs.objects.get(group_id = id)

	return render_to_response('work_with_us_group.html', locals(),\
    context_instance = RequestContext(request))

def day_regimen(request, id):
    mode_day = ModeDay.objects.get(group_id = id)

    return render_to_response('mode_day.html', locals(),\
    context_instance = RequestContext(request))    

def setka_zan(request, id):
    setzan = SetkaZan.objects.get(group_id = id)

    return render_to_response('setka_zan.html', locals(),\
    context_instance = RequestContext(request))    

def live_our_group(request, id):
    live_group = LiveOurGroups.objects.get(group_id = id)

    return render_to_response('live_our_group.html', locals(),\
    context_instance = RequestContext(request))

def sovet_group_educator(request, id):
    sovet_educator = SovetEducator.objects.get(group_id = id)

    return render_to_response('sovet_group_educator.html', locals(),\
    context_instance = RequestContext(request))
