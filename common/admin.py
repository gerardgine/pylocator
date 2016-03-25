from django.contrib import admin

from .models import StoragePlace, Box, ContactChannel, Receiver, SalesChannel, Sale, Item

admin.site.register(Item)
admin.site.register(Receiver)
admin.site.register(Sale)
admin.site.register(Box)
admin.site.register(SalesChannel)
admin.site.register(ContactChannel)
admin.site.register(StoragePlace)
