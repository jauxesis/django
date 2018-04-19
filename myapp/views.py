from __future__ import unicode_literals

from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import Context, loader

import datetime

def index(request):
    now = datetime.datetime.now()
    html = "<html><body><b>Its Django Dude!</b><br>It is now %s.</body></html>" % now
    return HttpResponse(html)

def home(request):
	# return render_to_response("myapp/templates/test.html")
	return render(request, 'test.html')