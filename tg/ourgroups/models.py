# -*- coding: utf-8 -*-
from django.db import models
from django_thumbs.db.models import ImageWithThumbsField
from tinymce.models import HTMLField

class Groups(models.Model):
    """ Модель Наши группы """
	
    name = models.CharField(u'Название', max_length=80)
    image = ImageWithThumbsField(verbose_name=u'изображение', help_text=u'Загрузите изображение группы',upload_to='uploads', blank=True, sizes=((200,200),(400,200)))
    text = HTMLField(u'текст')
    date_create = models.DateTimeField(u'Дата создания', auto_now=True)

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = u'Наши группы'
        verbose_name_plural = u'Наши группы'

class Group(models.Model):
    """ Модель Одиночных Групп """

    group = models.ForeignKey(Groups, verbose_name = 'Группа')
    text = HTMLField(u'Текст')
    

    def __unicode__(self):
        return '%s %s' % (u'Группа', self.group)

    class Meta:
        verbose_name = u'Группа'
        verbose_name_plural = u'Группа'

class WorkWithUs(models.Model):
    """ Модель - С нами работают """

    group = models.ForeignKey(Groups, verbose_name = 'Группа')
    text = HTMLField(u'Текст')
    

    def __unicode__(self):
        return '%s %s' % (u'С нами работают', self.group)

    class Meta:
        verbose_name = u'С нами работают'
        verbose_name_plural = u'С нами работают'

class ModeDay(models.Model):
    """ Модель - Режим дня """

    group = models.ForeignKey(Groups, verbose_name = 'Группа')
    text = HTMLField(u'Текст')
    

    def __unicode__(self):
        return '%s %s' % (u'Режим дня', self.group)

    class Meta:
        verbose_name = u'Режим дня'
        verbose_name_plural = u'Режим дня'        

class SetkaZan(models.Model):
    """ Модель - Сетка занятий """

    group = models.ForeignKey(Groups, verbose_name = 'Группа')
    text = HTMLField(u'Текст')
    

    def __unicode__(self):
        return '%s %s' % (u'Сетка занятий', self.group)

    class Meta:
        verbose_name = u'Сетка занятий'
        verbose_name_plural = u'Сетка занятий'        

class LiveOurGroups(models.Model):
    """ Модель - Жизнь наших групп """

    group = models.ForeignKey(Groups, verbose_name = 'Группа')
    text = HTMLField(u'Текст')
    

    def __unicode__(self):
        return '%s %s' % (u'Жизнь наших групп', self.group)

    class Meta:
        verbose_name = u'Жизнь наших групп'
        verbose_name_plural = u'Жизнь наших групп'   

class SovetEducator(models.Model):
    """ Модель - Советы воспитателя """

    group = models.ForeignKey(Groups, verbose_name = 'Группа')
    text = HTMLField(u'Текст')
    

    def __unicode__(self):
        return '%s %s' % (u'Советы воспитателя', self.group)

    class Meta:
        verbose_name = u'Советы воспитателя'
        verbose_name_plural = u'Советы воспитателя'           


    
        		        
		
