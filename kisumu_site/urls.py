from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings # new
from django.conf.urls.static import static
from users import views as user_views # new
from django.contrib.auth import views as auth_views



urlpatterns = [

    url(r'^$', include('posts.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^register/', user_views.register, name='register'),
    url(r'^login/', auth_views.LoginView.as_view(template_name ='users/login.html'), name='login'),
    url(r'^logout/', auth_views.LogoutView.as_view(template_name ='users/logout.html'), name='logout'),
    url(r'^posts/', include('posts.urls')),
        

]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)