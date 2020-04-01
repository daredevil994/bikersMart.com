from django.conf.urls import url
from signUpApp import views

app_name= 'signUpApp'
urlpatterns = [
    url(r'^$',views.sign_up_form_view,name='sign_up_form_view'),
]
