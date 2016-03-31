from django.contrib import admin

from .models import StoragePlace, Box, ContactChannel, Receiver, SalesChannel, Sale, Item, ItemStorage


class SaleInline(admin.StackedInline):
    model = Sale


class ItemStorageInline(admin.TabularInline):
    model = ItemStorage


class ItemStorageForBoxesInline(admin.TabularInline):
    model = ItemStorage
    fields = ("item",)
    extra = 1


class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "action", "has_sale", "sale_is_closed", "storage")
    search_fields = ["name"]
    list_filter = ("action",)
    inlines = (ItemStorageInline, SaleInline,)


class ReceiverAdmin(admin.ModelAdmin):
    list_display = ("__unicode__", "preferred_contact_channel")


class SaleAdmin(admin.ModelAdmin):
    list_display = ("__unicode__", "is_gift", "is_closed")
    list_filter = ("is_gift", "is_closed",)


class BoxAdmin(admin.ModelAdmin):
    list_display = ("name", "storage_place",)
    inlines = (ItemStorageForBoxesInline,)


admin.site.register(Item, ItemAdmin)
admin.site.register(Receiver, ReceiverAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Box, BoxAdmin)
admin.site.register(SalesChannel)
admin.site.register(ContactChannel)
admin.site.register(StoragePlace)
