from django.contrib import admin
from django.urls import path

from .views import NotesView, NoteView, AboutView

app_name = 'notebook'
urlpatterns = [
    path('notes/', NotesView.as_view(), name='notes'),
    path('note/<int:note_id>', NoteView.as_view(), name='note'),
    path('about/', AboutView.as_view(), name='about'),

]
