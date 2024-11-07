from django.db import models
from django.core.validators import MinValueValidator
from events.models import Event  # Assuming Event is in the same app or adjust import as needed.

class Ticket(models.Model):
    TICKET_TYPE_CHOICES = [
        ('VIP', 'VIP'),
        ('Standard', 'Standard'),
        ('Economy', 'Economy'),
    ]

    ticket_type = models.CharField(
        max_length=100,
        choices=TICKET_TYPE_CHOICES,
        default='Standard',
        help_text="Type of the ticket (e.g., VIP, Standard, Economy)."
    )
    description = models.TextField(
        default="",
        max_length=1000,
        help_text="A description of the ticket."
    )
    image = models.ImageField(
        upload_to='tickets/images/',
        blank=True,
        null=True,
        help_text="Optional image associated with the ticket."
    )
    amount = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0)],
        help_text="Amount of the ticket in the smallest currency unit (e.g., cents)."
    )
    quantity = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1)],
        help_text="Number of tickets available for this type."
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.SET_NULL,
        null=True,
        related_name='tickets',
        help_text="The event to which this ticket is linked."
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ticket_type} Ticket for {self.event} - {self.amount}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"
