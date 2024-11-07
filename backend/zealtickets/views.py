from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from datetime import datetime
from django.shortcuts import render
from events.models import Event
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate

def index(request):
    events = Event.objects.all()
    return render(request, 'index.html', {'events': events})

def events(request):
    return render(request, "events.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next', 'index')
                return redirect(next_url)
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def register(request):
        return render(request, 'registration/register.html')

@login_required
def ticket(request):
    return render(request, "ticket.html")
