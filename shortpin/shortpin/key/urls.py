from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^logic/', views.logic, name='logic'),
    url(r'^index/', views.index, name='index'),
    url(r'^grant_key/', views.grant_key, name='grant_key'),
    url(r'^key/(?P<key_id>[a-zA-Z0-9]+)/repay/', views.repay_key, name='repay_key'),
    url(r'^key/(?P<key_id>[a-zA-Z0-9]+)/', views.key_view, name='key_view'),
    url(r'^$', views.index)
]
