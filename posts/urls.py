from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^details/(?P<id>\d+)/$', views.details, name='details'),
  url(r'^contact/$', views.contact, name='contact'),
  url(r'^news/$', views.news, name='news' ),
  url(r'^tenders/$', views.tenders, name='tenders' ),
  url(r'^services/$', views.services, name='services' ),
  url(r'^ministries/$', views.ministries, name='ministries' ),
  url(r'^projects/$', views.projects, name='projects' ),
  url(r'^review/(?P<id>\d+)/$', views.review, name='review'),
  url(r'project/(?P<id>\d+)/comment/$', views.add_comment_to_project, name='add_comment_to_project'),
  
  

]