from rest_framework import generics
from .models import Event, Ticket
from .serializers import TicketSerializer
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

class TicketPurchaseView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

@login_required
def ticket_list(request):
    tickets = Ticket.objects.all()  # Fetch all tickets
    return render(request, 'tickets/ticket.html', {'tickets': tickets})
