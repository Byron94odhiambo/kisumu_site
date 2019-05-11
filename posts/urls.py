from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^details/(?P<id>\d+)/$', views.details, name='details'),
  url(r'^contact/$', views.contact, name='contact'),
  url(r'^news/$', views.news, name='news' ),
  url(r'^tenders/$', views.tenders, name='tenders' ),
  

]