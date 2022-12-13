from django.contrib import admin

from .models import Flat

class FlatAdmin(admin.ModelAdmin):
    

admin.site.register(Flat)
