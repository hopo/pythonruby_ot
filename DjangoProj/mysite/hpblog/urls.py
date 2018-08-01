from django.conf.urls import url
from .views import board_list, board_item, board_insert, board_update

urlpatterns = [
    url(r'^$', board_list, name='board_list'),
    url(r'^insert$', board_insert, name='board_insert'),
    url(r'^item/$', board_item, name='board_item'),
    url(r'^item/(?P<p_id>[\d]+)/$', board_item, name='board_item'),
    url(r'^update/$', board_update, name='board_update'),
    url(r'^update/(?P<p_id>[\d]+)/$', board_update, name='board_update'),
    url(r'^update/(?P<p_id>[\d]+)/proc$', board_update, name='board_update'),
]
