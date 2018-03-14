from django.conf.urls import url
from djangoApp import views

urlpatterns = [
    url(r'time/$', views.today_is, name='todays_time'),
    url(r'^$', views.index, name='djangoApp_index'),
]