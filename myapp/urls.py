from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^home',views.home,name='home'),
    url(r'^welcome',views.welcome,name='welcome'),
    url(r'^s3',views.uploads3,name='s3'),
    url(r'^files',views.getFiles,name='getFiles'),
]