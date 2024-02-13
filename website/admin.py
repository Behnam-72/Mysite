from django.contrib import admin
from website.models import Contact, Newsletter

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'creaded_date'
    empty_value_display = "-empty-"
    list_display = ['name', 'email', 'subject', 'creaded_date', 'updated_date']
    ordering = ('creaded_date',)
    search_fields = ['name', 'subject']
    list_filter = ['name']

admin.site.register(Contact, ContactAdmin)
admin.site.register(Newsletter)
# Register your models here.
