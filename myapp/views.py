from __future__ import unicode_literals

from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response

from django.template import Context, loader
import sys
import datetime
from PIL import Image
import urlparse
from django.template.loader import get_template
from io import BytesIO
import xhtml2pdf.pisa as pisa # pip install xhtml2pdf
def index(request):
    now = datetime.datetime.now()
    html = "<html><body><b>Its Django Dude!</b><br>It is now %s.</body></html>" % now
    return HttpResponse(html)

def home(request):
	# return render_to_response("myapp/templates/test.html")
	return render(request, 'test.html')

def welcome(request):
	html = "<html><body>Its Welcome Page</body></html>"
	return HttpResponse(html)

def uploads3(request):
	return render(request,'s3.html',{"formTitle":"AWS S3 Bucket File Uplaod"})

def getFiles(request, status=200, **kwargs):
	# /home/auxesis/Pictures pip install pillow
	# jpgfile = Image.open("/home/auxesis/Pictures/a.png") # http://localhost:8088/myapp/files?path=/sdf/asdf/ds/f.png
	# for png https://pypi.org/project/svglib/ mime: content_type="image/png"
	# for jpg/jpeg https://pypi.org/project/svglib/ mime: content_type="image/jpg"
	# path = "/home/auxesis/Pictures/a.png"
	print request.path
	pathGET = request.GET['path']
	print "GETunicode", pathGET
	lastExtensionArr = pathGET.split('.')
	ext = (lastExtensionArr[-1]).lower()
	extArr1 = ['png', 'jpeg', 'jpg']
	extArr2 = ['pdf']
	contentType = "image/png" # "image/jpeg"
	responseFileType = "PNG" # "JPEG"
	typeOfMedia = 'img'
	if any(ext in s for s in extArr1):
		typeOfMedia = 'img'
		contentType = "image/" + ext # "image/jpeg"
		responseFileType = ext.upper()
	if any(ext in s for s in extArr2):
		typeOfMedia = 'pdf'
		contentType = "application/" + ext # "image/jpeg"
		responseFileType = ext.upper()
	print 'response:::::',responseFileType,contentType
	try:
		if typeOfMedia is 'img':
			jpgfile = Image.open(pathGET)
			response = HttpResponse(content_type=contentType)
			jpgfile.save(response, responseFileType)
			return response
		else:
			image_data = open(pathGET, "rb").read()
			return HttpResponse(image_data, content_type=contentType)
	    	
	except IOError as e:
		# print "error:",e
	    red = Image.new('RGBA', (100, 100), (255,120,110,0))
	    response = HttpResponse(content_type="image/png")
	    red.save(response, "PNG")
	    return response