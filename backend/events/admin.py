from django.contrib import admin
from .models import Event, Category

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'date', 'location')
    search_fields = ('name', 'category__name', 'location')
    list_filter = ('category', 'date')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Event, EventAdmin)
admin.site.register(Category, CategoryAdmin)