from rest_framework import generics
from .models import Event, Ticket
from .serializers import TicketSerializer
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class TicketPurchaseView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

@login_required
def ticket_list(request):
    tickets = Ticket.objects.filter(user=request.user)  # Fetch tickets for the logged-in user
    return render(request, 'tickets/ticket.html', {'tickets': tickets})
