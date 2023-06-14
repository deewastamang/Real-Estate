from django.contrib import admin
from .models import Realtor
# Register your models here.


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'hire_date', 'is_som')
    list_filter = ('name',)
    list_editable = ('is_som',)
    search_fields = ('name', 'email', 'phone')
    list_per_page = 20


admin.site.register(Realtor, RealtorAdmin)
