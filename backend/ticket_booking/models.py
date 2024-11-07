from django.db import models
from events.models import Event  # Assuming you have an Event model in your events app

class TicketBooking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    number_of_tickets = models.IntegerField()
    payment_choice = models.CharField(max_length=50, choices=[('card', 'Credit/Debit Card'), ('paypal', 'PayPal'), ('cash', 'Cash')])
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.customer_name} for {self.event.name}"
