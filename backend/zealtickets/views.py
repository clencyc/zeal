from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from datetime import datetime
from django.shortcuts import render

def index(request):
    return render(request, "index.html")
