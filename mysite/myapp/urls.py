from . import views
#from django.urls import path
from django.conf.urls import include, url 

urlpatterns = [
    url('', views.index, name='index'),
]
