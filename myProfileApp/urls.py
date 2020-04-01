from django.conf.urls import url
from myProfileApp import views

app_name='myProfileApp'

urlpatterns = [
    url(r'^$',views.my_profile,name='my_profile'),
    url(r'^settings&privacy/',views.settings_view,name='settings_view'),
]
