from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.board_list, name='board_list'),
    url(r'^insert/$', views.board_insert, name='board_insert'),
    url(r'^item/$', views.board_item, name='board_item'),
]
