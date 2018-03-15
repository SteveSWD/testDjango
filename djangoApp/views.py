# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import datetime
from django import template

def index(request):
    return HttpResponse("Hello Django")

def today_is(request):
    now = datetime.datetime.now()
    t = template.loader.get_template('djangoApp/datetime.html')
    c = {'now': now}
    html = t.render(c)
    return HttpResponse(html)