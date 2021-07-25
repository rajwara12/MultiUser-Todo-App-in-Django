from django.contrib import admin

from . models import Todo, Blog
# Register your models here.

admin.site.register(Todo)
admin.site.register(Blog)
