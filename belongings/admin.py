from django.contrib import admin

from .models import StoragePlace, Box, ContactChannel, Receiver, SalesChannel, Sale, Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "action")
    search_fields = ["name"]
    list_filter = ("action",)


class ReceiverAdmin(admin.ModelAdmin):
    list_display = ("__unicode__", "preferred_contact_channel")


class SaleAdmin(admin.ModelAdmin):
    list_display = ("__unicode__", "is_closed")
    list_filter = ("is_closed",)


class ItemInline(admin.TabularInline):
    model = Item
    extra = 1


class BoxAdmin(admin.ModelAdmin):
    list_display = ("name", "storage_place")
    inlines = (ItemInline,)


admin.site.register(Item, ItemAdmin)
admin.site.register(Receiver, ReceiverAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Box, BoxAdmin)
admin.site.register(SalesChannel)
admin.site.register(ContactChannel)
admin.site.register(StoragePlace)
