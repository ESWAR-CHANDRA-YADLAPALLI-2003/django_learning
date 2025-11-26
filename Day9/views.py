from datetime import timezone
from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.sessions.models import Session
from .forms import RegisterForm
def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created. Please log in.")
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'Day9/register.html', {'form': form})

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # debug prints (remove in production)
        print("LOGIN ATTEMPT:", username)

        user = authenticate(request, username=username, password=password)
        print("AUTHENTICATE:", user)

        if user is not None:
            login(request, user)                     # creates session
            request.session['username'] = user.username  # optional custom session data
            messages.success(request, f"Welcome {user.username}!")
            return redirect('dashboard')             # redirect to dashboard
        else:
            messages.error(request, "Invalid username or password")
            return render(request, 'Day9/login.html')
    return render(request, 'Day9/login.html')


def logout_user(request):
    logout(request)                 # clears session
    messages.info(request, "You have been logged out.")
    return redirect('login')


@login_required(login_url='login')
def dashboard(request):
    # you can access request.user and session
    username = request.user.username
    return render(request, 'Day9/dashboard.html', {'username': username})


def set_session_example(request):
    # set session values
    request.session['fav_color'] = 'blue'           # simple key/value
    request.session['visited_on'] = str(timezone.now())
    request.session['visits'] = request.session.get('visits', 0) + 1

    # optionally set expiry (seconds)
    # request.session.set_expiry(3600)  # expires in 1 hour

    return render(request, 'day9/session_set.html', {
        'visits': request.session['visits'],
    })

def get_session_example(request):
    fav = request.session.get('fav_color', 'not set')
    visited = request.session.get('visited_on', 'never')
    return render(request, 'day9/session_get.html', {
        'fav': fav,
        'visited': visited,
    })

def clear_session(request):
    # Remove a single key
    request.session.pop('fav_color', None)
    # or clear all session keys for current session
    # request.session.flush()
    return redirect('day9:session_get')
def home_view(request):
    return render(request, 'Day9/home.html')

def about_view(request):
    return render(request, 'Day9/about.html')

def contact_view(request):
    return render(request, 'Day9/contact.html')