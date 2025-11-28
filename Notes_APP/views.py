from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from .models import Note
from .forms import NoteForm

class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'Notes_APP/note_list.html'
    context_object_name = 'notes'
    paginate_by = 6
    login_url = '/accounts/login/'

    def get_queryset(self):
        qs = Note.objects.filter(owner=self.request.user)
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(Q(title__icontains=q) | Q(description__icontains=q))
        # staff with permission can see all
        if self.request.user.has_perm('Notes_APP.view_all_notes'):
            qs = Note.objects.all().order_by('-created_at')
        return qs

class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'Notes_APP/note_detail.html'
    context_object_name = 'note'
    login_url = '/accounts/login/'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.owner != self.request.user and not self.request.user.has_perm('Notes_APP.view_all_notes'):
            raise PermissionDenied
        return obj

class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'Notes_APP/note_form.html'
    success_url = reverse_lazy('notes:list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'Notes_APP/note_form.html'
    success_url = reverse_lazy('notes:list')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.owner != self.request.user:
            raise PermissionDenied
        return obj

class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'Notes_APP/note_confirm_delete.html'
    success_url = reverse_lazy('notes:list')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.owner != self.request.user:
            raise PermissionDenied
        return obj
