from django.contrib import admin
from .models import Event, Category

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'date', 'location', 'image')
    search_fields = ('name', 'category__name', 'location')
    list_filter = ('category', 'date')

    # Detail view configuration
    fieldsets = (
        (None, {
            'fields': ('name', 'category', 'date', 'location', 'image')
        }),
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Event, EventAdmin)
admin.site.register(Category, CategoryAdmin)