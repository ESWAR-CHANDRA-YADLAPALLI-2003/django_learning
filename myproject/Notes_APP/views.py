from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm
from django.contrib import messages

# Dashboard
@login_required
def dashboard(request):
    total_notes = Note.objects.filter(user=request.user).count()
    return render(request, "Notes_APP/dashboard.html", {"total_notes": total_notes})

# List All Notes
@login_required
def notes_list(request):
    notes = Note.objects.filter(user=request.user).order_by('-created_at')
    return render(request, "Notes_APP/notes_list.html", {"notes": notes})

# Create Note
@login_required
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            messages.success(request, "Note created successfully.")
            return redirect('notes:list')
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})

# Edit Note
@login_required
def note_edit(request, id):
    note = get_object_or_404(Note, id=id, user=request.user)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('Notes_APP/notes_list')
    else:
        form = NoteForm(instance=note)

    return render(request, "Notes_APP/note_edit.html", {"form": form})

# Delete Note
@login_required
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        note.delete()
        messages.warning(request, "Note deleted.")
        return redirect('notes:list')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})
# Note Update
@login_required
def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, "Note updated successfully.")
            return redirect('notes:detail', pk=note.pk)
        else:
            messages.error(request, "Please correct the highlighted errors.")
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form})

