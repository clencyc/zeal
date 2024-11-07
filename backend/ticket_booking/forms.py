from django import forms
from .models import TicketBooking

class TicketBookingForm(forms.ModelForm):
    class Meta:
        model = TicketBooking
        fields = ['customer_name', 'number_of_tickets', 'payment_choice']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-input border rounded-md py-2 px-3 focus:ring-2 focus:ring-blue-500'}),
            'number_of_tickets': forms.NumberInput(attrs={'class': 'form-input border rounded-md py-2 px-3 focus:ring-2 focus:ring-blue-500'}),
            'payment_choice': forms.Select(attrs={'class': 'form-input border rounded-md py-2 px-3 focus:ring-2 focus:ring-blue-500'}),
        }
