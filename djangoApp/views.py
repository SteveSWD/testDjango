# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import datetime
from django import template
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello Django")

def today_is(request):
    now = datetime.datetime.now()
    #t = template.loader.get_template('djangoApp/time.html')
    #c = {'now': now}
    #html = t.render(c)
    #return HttpResponse(html)
    return render (request, 'djangoApp/datetime.html', {
        'now': now,
        'template_name': 'djangoApp/nav.html'
    })