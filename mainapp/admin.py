from django.contrib import admin
# Register your models here.
from .models import Todo


class Todo_list(admin.ModelAdmin):
    list_display = ['added_date', 'text']


admin.site.register(Todo, Todo_list)
