from django.conf.urls import url
from galleryApp import views

app_name= 'galleryApp'

urlpatterns = [
    url(r'^$',views.index,name='index'),
]
