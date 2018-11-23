#!/usr/bin/env python
# -*- coding: utf-8 -*-  
'''
@author: xiaoshui
@contact: deamoncao100@gmail.com
@file: forms.py
@time: 2018/11/19 16:39
@desc:
'''

from django import forms
from .models import ArticlePost

class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = ArticlePost
        fields = ('title','body')

