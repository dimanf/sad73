# -*- coding: utf-8 -*-
from django import forms

class qaform(forms.Form):
    """docstring for qaform"""
    name = forms.CharField(error_messages={'required': 'Имя обязательное поле.'}, widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'E-mail'}), required=False)
    text = forms.CharField(error_messages={'required': 'Введите текст вопроса.'}, widget=forms.Textarea)

    		

	
