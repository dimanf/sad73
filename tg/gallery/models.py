# -*- coding: utf-8 -*-
from django.db import models
from django_thumbs.db.models import ImageWithThumbsField

class Gallery(models.Model):
    """docstring for Gallery"""
	
    name = models.CharField(u'Фотогалерея', max_length = 30)
    face = ImageWithThumbsField(verbose_name=u'изображение', upload_to='uploads', blank=True, sizes=((200,200),(800,600)))
    date_create = models.DateTimeField(u'Дата создания', auto_now=True)

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = u'фотогалерея'
        verbose_name_plural = u'фотогалереи'

class Image(models.Model):
    
    image = ImageWithThumbsField(u'изображение', upload_to='uploads', blank=True, sizes=((200,200),(800,600)))
    gallery = models.ForeignKey(Gallery, verbose_name = 'Галерея')

    def __unicode__(self):
        return '%s %s' % (u'Изображение для галереи', self.gallery)

    class Meta:
        verbose_name = u'изображение'
        verbose_name_plural = u'изображения'
        		        
		
