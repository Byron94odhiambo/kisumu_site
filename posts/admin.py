from django.contrib import admin

# Register your models here.
from .models import Posts,  Adverts

admin.site.register(Posts)
admin.site.register(Adverts)
