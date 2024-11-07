from django.shortcuts import render, get_object_or_404, redirect
from .forms import TicketBookingForm
from events.models import Event  # Assuming you have an Event model in your events app

def ticket_booking_view(request, event_id):
    event = get_object_or_404(Event, id=event_id)  # Fetch the event by ID
    if request.method == 'POST':
        form = TicketBookingForm(request.POST)
        if form.is_valid():
            # Save the booking and associate it with the event
            booking = form.save(commit=False)
            booking.event = event
            booking.save()
            return redirect('booking-success')  # Redirect to success page after booking
    else:
        form = TicketBookingForm()

    return render(request, 'ticket_booking/book_ticket.html', {'event': event, 'form': form})


def booking_success(request):
    return render(request, 'ticket_booking/booking_success.html')
