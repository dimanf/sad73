# -*- coding: utf-8 -*-
from django.db import models
from tinymce.models import HTMLField

class qamodel(models.Model):
	"""docstring for qa"""

	NEWS_STATUS_CHOICES = (
        ('public', u'Опубликовано'),
        ('draft', u'Черновик'),
    )

	name = models.CharField(u'Имя', max_length = 30)
	email = models.EmailField(u'email', blank = True)
	text = HTMLField(u'Текст')
	date_create = models.DateTimeField(u'Дата создания', auto_now=True)
	status = models.CharField(u'статус', max_length=6, choices=NEWS_STATUS_CHOICES, help_text=u'Если черновик, то вопрос на сайте не выводится')

	def __unicode__(self):
		return "%s" % self.name

	class Meta:
		verbose_name = u'Вопрос-ответ'
		verbose_name_plural = u'Вопрос-ответ'	


		
