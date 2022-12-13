from django.contrib import admin

from .models import Flat


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['description', 'town', 'town_district', 'address']


admin.site.register(Flat, FlatAdmin)
