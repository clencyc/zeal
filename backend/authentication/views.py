# Import necessary modules and models
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import CustomUser
from .forms import CustomUserCreationForm

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if not CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Invalid Email')
            return redirect('/login/')
        
        user = authenticate(email=email, password=password)
        
        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('ticket_list')
    
    return render(request, 'registration/login.html')
# Define a view function for the registration page
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "Account created successfully!")
                return redirect('ticket_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def ticket(request):
    return render(request, 'tickets/ticket.html')



