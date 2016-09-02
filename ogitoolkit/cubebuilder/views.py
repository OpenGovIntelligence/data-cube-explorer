#-*- coding: utf-8 -*-

import os

import json

from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect


def index(request):

    template_name = 'cubebuilder/index.html'

    context = {

    }

    return render(request, template_name, context)
