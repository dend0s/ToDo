from django.contrib import admin
from .models import ToDo


class ToDoAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'content')


admin.site.register(ToDo, ToDoAdmin)
