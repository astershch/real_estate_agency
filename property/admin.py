from django.contrib import admin

from .models import Flat, Complaint


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat', 'user')


class FlatAdmin(admin.ModelAdmin):
    raw_id_fields = ('like',)

    search_fields = (
        'description',
        'town',
        'town_district',
        'address',
    )

    readonly_fields = ('created_at',)

    list_display = (
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',
    )

    list_editable = ('new_building',)

    list_filter = (
        'new_building',
        'rooms_number',
        'has_balcony',
    )


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
