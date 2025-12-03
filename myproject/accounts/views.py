from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.http import require_http_methods
def home(request):
    return render(request, "home.html")
def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    return render(request, "register.html", {"form": form})
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        print("USERNAME:", username)
        print("PASSWORD:", password)

        user = authenticate(request, username=username, password=password)
        print("USER OBJECT:", user)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})
    return render(request, "accounts/login.html")
@login_required(login_url="/login/")
def dashboard(request):
    username = request.session.get('username')    # SESSION ACCESS
    return render(request, "dashboard.html")
@require_http_methods(["GET", "POST"])
def logout_user(request):
    logout(request)
    request.session.flush()
    return redirect("home")
def is_staff(user):
    return user.is_staff

@user_passes_test(is_staff)
def staff_page(request):
    return render(request, "staff_page.html")
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, "welcome.html")   # <- WHAT DO YOU HAVE HERE?
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")
    return render(request, "accounts/login.html")
