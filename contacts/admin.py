from django.contrib import admin
from django.db import models
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'contact_date', 'email')
    list_display_links = ('id', 'name')
    list_per_page = 25
    search_fields = ('name', 'email', 'listing')

# Register your models here.
admin.site.register(Contact)
