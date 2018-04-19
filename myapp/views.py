from django.shortcuts import render
from __future__ import unicode_literals
# Create your views here.
from django.http import HttpResponse

from django.shortcuts import get_object_or_404
from django.template import loader
from django.shortcuts import render_to_response

import datetime

def index(request):
    now = datetime.datetime.now()
    html = "<html><body><b>Its Django Dude!</b><br>It is now %s.</body></html>" % now
    return render_to_response('test.html')

def home(request):
	return HttpResponse("Hello django")