from django.contrib import admin
from .models import Contact

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'listing', 'phone', 'user_id', 'contact_date')
    list_display_links = ('name', 'listing', 'user_id')
    list_filter = ('name',)
    search_fields = ('name', 'email', 'phone', 'listing',)


admin.site.register(Contact, ContactAdmin)
