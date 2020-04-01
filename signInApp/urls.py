from django.conf.urls import url
from signInApp import views

app_name= 'signInApp'

urlpatterns = [
    url(r'^$',views.user_login,name='user_login'),
]
