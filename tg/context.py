# -*- coding: utf-8 -*-

def menu_processor(request):
    path = request.path.split('/')[1]
    return {
        'path': path,
    }