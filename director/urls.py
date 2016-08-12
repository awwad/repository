from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^Enroll$', views.Enroll, name='Enroll'),
    url(r'^List$', views.List, name='List'), 
]
