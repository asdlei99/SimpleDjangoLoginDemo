#_*_coding:UTF-8_*_

from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'^login/$', views.login_page),
    url(r'^login_submit/', views.login_submit),
    #url(r'^$', views.),
]