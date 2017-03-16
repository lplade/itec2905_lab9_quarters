from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.quarter_list, name='quarter_list'),
    url(r'^quarter/(?P<pk>\d+)/$', views.quarter_detail, name='quarter_detail'),
]
