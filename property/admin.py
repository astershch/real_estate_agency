from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)

    list_display = (
        'full_name',
        'phonenumber',
        'pure_phone',
    )


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat', 'user')


class OwnerInline(admin.TabularInline):
    model = Owner.flats.through

    raw_id_fields = ('owner', 'flat')


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

    inlines = [OwnerInline]


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
