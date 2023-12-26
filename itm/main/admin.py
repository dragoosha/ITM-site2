from django.contrib import admin

from .models import Contacts


class ContactsView(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'firma', 'position', 'telefon', 'place', 'country', 'email', 'plz', 'time_create')
    list_display_links = ('id', 'name', 'surname', 'firma', 'position', 'telefon', 'place', 'country', 'email', 'plz', 'time_create')
    search_fields = ('id', 'name', 'surname', 'firma', 'position', 'telefon', 'place', 'country', 'email', 'plz', 'time_create')


admin.site.register(Contacts, ContactsView)
