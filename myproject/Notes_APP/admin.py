from django.contrib import admin
from .models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_favorite', 'created_at')  # changed owner → user
    search_fields = ('title', 'description', 'user__username')       # changed owner__username → user__username
    list_filter = ('is_favorite', 'created_at')
