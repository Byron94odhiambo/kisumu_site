from django.contrib import admin

# Register your models here.
from .models import Posts,  Adverts,Projects, Comment

admin.site.register(Posts)
admin.site.register(Adverts)
admin.site.register(Projects)
admin.site.register(Comment)
admin.site.site_header = 'Administration'
