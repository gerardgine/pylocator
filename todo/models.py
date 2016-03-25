from __future__ import unicode_literals

from django.db import models


class Executor(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    executor = models.ForeignKey(Executor, on_delete=models.SET_NULL, null=True, blank=True)
    place = models.CharField(max_length=200)
    due_date = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title
