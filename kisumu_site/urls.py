from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings # new
from django.conf.urls.static import static # new



urlpatterns = [

    url(r'^$', include('posts.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^posts/', include('posts.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),    

]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)