from django.contrib import admin

from .models import Executor, Todo


admin.site.register(Executor)
admin.site.register(Todo)
