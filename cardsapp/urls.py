from django.urls import path
from . import views

urlpatterns = [
    path('api/profiles/', views.ProfileList.as_view()),
    path('api/flashcards/', views.FlashcardList.as_view()),
    path('api/notes/', views.NoteList.as_view()),
    path('api/profile/profile-id/(?P<pk>[0-9]+)/$',views.ProfileList.as_view()),
    path('api/flashcards/flashcards-id/(?P<pk>[0-9]+)/$',views.FlashcardList.as_view()),
    path('api/notes/notes-id/(?P<pk>[0-9]+)/$',views.ProfileList.as_view())
]
