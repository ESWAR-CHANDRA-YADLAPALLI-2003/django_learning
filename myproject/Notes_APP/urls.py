from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),

    path('notes/', views.notes_list, name='notes_list'),
    path('notes/create/', views.note_create, name='note_create'),
    path('notes/edit/<int:id>/', views.note_edit, name='note_edit'),
    path('notes/delete/<int:id>/', views.note_delete, name='note_delete'),
]
