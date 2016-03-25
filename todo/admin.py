from django.contrib import admin

from .models import Executor, Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ("title", "executor", "due_date", "is_completed")
    list_filter = ("executor", "is_completed")


admin.site.register(Executor)
admin.site.register(Todo, TodoAdmin)
