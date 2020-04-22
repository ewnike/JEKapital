from django.contrib import admin
from django.contrib.auth.models import *
# Register your models here.
from .models import Property, Contact


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on', 'image')
    list_filter = ("status",)
    search_fields = ['title', 'content', 'street_address', 'neighborhood', 'zipcode']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Property, PropertyAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'message')
    search_fields = ['first_name', 'last_name', 'email', 'message']

admin.site.register(Contact, ContactAdmin)
