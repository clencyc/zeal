from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import Event
from .serializers import EventSerializer

def event_list_view(request):
    events = Event.objects.all()
    return render(request, 'events/events.html', {'events': events})


def ticket_booking_view(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    # Logic for ticket booking here
    return render(request, 'ticket_booking.html', {'event': event})

class EventListView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
