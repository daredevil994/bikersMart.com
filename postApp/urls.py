from django.conf.urls import url
from postApp import views

app_name='postApp'

urlpatterns = [
    url(r'^post_view/',views.create_post,name='post_view'),
]
