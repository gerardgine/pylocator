from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError


ACTIONS_CHOICES = [
    (b'not_decided', b'Not decided yet'),
    (b'relocate', b'Relocate'),
    (b'store', b'Store'),
    (b'sell', b'Sell'),
    (b'give', b'Give'),
]


class StoragePlace(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Box(models.Model):
    name = models.CharField(max_length=100)
    storage_place = models.ForeignKey(StoragePlace, on_delete=models.SET_NULL, related_name="boxes", null=True,
                                      blank=True)
    # measures?
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "boxes"

    def __unicode__(self):
        return self.name


class ContactChannel(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Receiver(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    preferred_contact_channel = models.ForeignKey(ContactChannel, on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        if not self.name:
            return self.username
        elif not self.username:
            return self.name
        else:
            return "{} ({})".format(self.name, self.username)

    def clean(self):
        if self.name is None and self.username is None:
            raise ValidationError("Either 'name' or 'username' must be specified")
        return


class SalesChannel(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Sale(models.Model):
    sales_channel = models.ForeignKey(SalesChannel, on_delete=models.PROTECT)
    url = models.URLField(null=True, blank=True)
    desired_price = models.FloatField(default=0.0)
    final_price = models.FloatField(null=True, blank=True)
    buyer = models.ForeignKey(Receiver, on_delete=models.PROTECT, null=True, blank=True)
    is_closed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "{} ({})".format(self.item, self.sales_channel)


class Item(models.Model):
    name = models.CharField(max_length=100)
    original_price = models.FloatField(default=0.0)
    action = models.CharField(max_length=20, choices=ACTIONS_CHOICES, default='relocate', null=True, blank=True)
    box = models.ForeignKey(Box, on_delete=models.SET_NULL, related_name="items", null=True, blank=True)
    storage_place = models.ForeignKey(StoragePlace, on_delete=models.SET_NULL, related_name="items", null=True,
                                      blank=True)
    receiver = models.OneToOneField(Receiver, on_delete=models.SET_NULL, related_name="free_items", null=True,
                                    blank=True)
    sale = models.OneToOneField(Sale, on_delete=models.SET_NULL, related_name="item", null=True, blank=True)
    # measures?
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

