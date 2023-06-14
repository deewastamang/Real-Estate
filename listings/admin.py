from django.contrib import admin

from .models import Listing
# Register your models here.


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'realtor', 'address', 'status', 'is_published')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('status', 'is_published')
    search_fields = ('title', 'address', 'city', 'zipcode', 'price')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
