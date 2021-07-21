from django.urls import path
from . import views

urlpatterns = [
    path('api/profiles/', views.ProfileList.as_view()),
    path('api/flashcards/', views.FlashcardList.as_view()),
    path('api/notes/', views.NoteList.as_view()),
]