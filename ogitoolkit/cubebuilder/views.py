#-*- coding: utf-8 -*-

import os

import json

from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render, redirect

try: 
  from urllib2 import urlopen
  from urllib2 import Request
  from urlparse import scheme_chars
  unicode = unicode
except ImportError: 
  from urllib.request import urlopen

def call_api(request, api_name):
    try:
        url = settings.API_URL + api_name + "?" + request.GET.urlencode()
        res = urlopen(url)
        data = json.loads('{ "result" :'+ res.read() + "}")
        data["sucess"] = True
        response =  JsonResponse(data)
        return response
    except Exception as e:
        return JsonResponse({'success': False, "message" : str(e)})

def index(request):

    template_name = 'cubebuilder/index.html'

    context = {

    }

    return render(request, template_name, context)
