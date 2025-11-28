from django.contrib import admin
from .models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'is_favorite', 'created_at')
    search_fields = ('title', 'description', 'owner__username')
    list_filter = ('is_favorite', 'created_at')
