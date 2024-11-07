from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from datetime import datetime
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def events(request):
    return render(request, "events.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

# def ticket(request):
#     return render(request, "ticket.html")

