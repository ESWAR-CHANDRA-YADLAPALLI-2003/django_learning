# Day9/views.py
from datetime import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import RegisterForm, TaskForm
from .models import Task

User = get_user_model()

# -----------------------------------------
# Authentication Views
# -----------------------------------------
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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome {user.username}!")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'Day9/login.html')


def logout_user(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')


# -----------------------------------------
# Static Pages
# -----------------------------------------
def home_view(request):
    return render(request, 'Day9/home.html')


def about_view(request):
    return render(request, 'Day9/about.html')


def contact_view(request):
    return render(request, 'Day9/contact.html')


# -----------------------------------------
# Dashboard
# -----------------------------------------
@login_required(login_url='login')
def dashboard(request):
    tasks = Task.objects.filter(owner=request.user)
    return render(request, 'Day9/dashboard.html', {'tasks': tasks})


# -----------------------------------------
# Task Views - Class-based
# -----------------------------------------
class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'Day9/task_list.html'
    context_object_name = 'tasks'
    login_url = 'login'

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)


class TaskCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'Day9/task_form.html'
    success_url = '/Day9/dashboard/'

    # Only users with 'add_task' permission can access
    permission_required = 'Day9.add_task'
    raise_exception = True  # Returns 403 Forbidden instead of redirect


    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'Day9/task_form.html'
    success_url = reverse_lazy('dashboard')
    login_url = 'login'


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'Day9/task_confirm_delete.html'
    success_url = reverse_lazy('dashboard')
    login_url = 'login'


# -----------------------------------------
# Task Edit - Function-based (optional)
# -----------------------------------------
@permission_required('Day9.change_task', login_url='login', raise_exception=True)
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TaskForm(instance=task)
    return render(request, 'Day9/task_form.html', {'form': form})


# -----------------------------------------
# Session Examples
# -----------------------------------------
def set_session_example(request):
    request.session['fav_color'] = 'blue'
    request.session['visited_on'] = str(timezone.now())
    request.session['visits'] = request.session.get('visits', 0) + 1
    return render(request, 'Day9/session_set.html', {'visits': request.session['visits']})


def get_session_example(request):
    fav = request.session.get('fav_color', 'not set')
    visited = request.session.get('visited_on', 'never')
    return render(request, 'Day9/session_get.html', {'fav': fav, 'visited': visited})


def clear_session(request):
    request.session.pop('fav_color', None)
    request.session.pop('visited_on', None)
    request.session.pop('visits', None)
    return redirect('session_get')
