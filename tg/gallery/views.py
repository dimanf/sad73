# -*- coding: utf-8 -*-
import datetime

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

from gallery.models import Gallery, Image

def gallery(request):
	
    gallery_list = Gallery.objects.all()

    return render_to_response('gallery.html', locals(),\
    context_instance = RequestContext(request))

def gallery_request(request, gallery_id):
    
    gallery_id = int(gallery_id)
    gallery_list = Gallery.objects.filter(id = gallery_id)

    photos_list = Image.objects.filter(gallery_id = gallery_id)
    
    pagenation = Paginator(photos_list, 12)
    photo_count = pagenation.count
    
    page = request.GET.get('page', 1)
    page = int(page)
    
    range_next = []
    range_prev = []   
    
    try:
        photo_page = pagenation.page(page)
        range_next = pagenation.page_range[page:page+5]        
        
        if page > 5:
            range_prev = pagenation.page_range[page-6:page-1]
        else:
            range_prev = pagenation.page_range[:page-1]
            
    except EmptyPage:
        photo_page = pagenation.page(pagenation.num_pages)
        
        if page > 5:
            range_prev = pagenation.page_range[page-6:page-1]
        else:
            range_prev = pagenation.page_range[:page-1]            
    
    next = len(range_next)
    prev = len(range_prev)

    return (render_to_response('gallery_request.html', locals(),
    context_instance = RequestContext(request)))


