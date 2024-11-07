# admin.py
from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    # List view configuration
    list_display = ('ticket_type', 'event', 'amount', 'quantity', 'created_at')
    list_filter = ('ticket_type', 'event', 'created_at')
    search_fields = ('ticket_type', 'event__name', 'description')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

    # Detail view configuration
    fieldsets = (
        (None, {
            'fields': ('ticket_type', 'event', 'amount', 'quantity', 'description', 'image')
        }),
        ('Dates', {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at',)
