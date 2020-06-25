from django.contrib import admin
from .models import Todo


class TodoAmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)


admin.site.register(Todo, TodoAmin)