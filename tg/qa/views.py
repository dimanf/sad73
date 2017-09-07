# -*- coding: utf-8 -*-
import datetime

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse, HttpResponseRedirect
# from django.core.mail import send_mail
# from django.contrib.auth import logout
from qa.forms import qaform
from qa.models import qamodel

def qa(request):
    if request.method == 'POST':
        form = qaform(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            q_a = qamodel(name = cd['name'],
				     email = cd['email'],
				     text = cd['text'])
            q_a.save()
            return HttpResponseRedirect('%s' % request.path)
    else:
        form = qaform()

    quest_answ = qamodel.objects.filter(status = 'public')	

    pagenation = Paginator(quest_answ, 10)
    quest_count = pagenation.count
    
    page = request.GET.get('page', 1)
    page = int(page)
    
    range_next = []
    range_prev = []   
    
    try:
        quest_page = pagenation.page(page)
        range_next = pagenation.page_range[page:page+5]        
        
        if page > 5:
            range_prev = pagenation.page_range[page-6:page-1]
        else:
            range_prev = pagenation.page_range[:page-1]
            
    except EmptyPage:
        quest_page = pagenation.page(pagenation.num_pages)
        
        if page > 5:
            range_prev = pagenation.page_range[page-6:page-1]
        else:
            range_prev = pagenation.page_range[:page-1]            
    
    next = len(range_next)
    prev = len(range_prev)	

    quest_answer = qamodel.objects.all()			
    return render_to_response('qa.html', locals(),\
    context_instance = RequestContext(request))

