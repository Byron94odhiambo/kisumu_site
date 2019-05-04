from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [

    url(r'^$', include('posts.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^posts/', include('posts.urls')),
]
