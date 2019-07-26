from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^currency_table/$', views.currency_table, name='currency_table'),
    url(r'exchange/$', views.exchange, name='exchange'),
    url(r'exchange_table/$', views.exchange_table, name='exchange_table'),
]