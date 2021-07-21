from django.conf.urls import url
from flashapp import views


urlpatterns = [
    
    url(r'^api/profiles/', views.ProfileList.as_view()),
    url(r'^api/flashcards/', views.FlashcardList.as_view()),
    url(r'^api/notes/', views.NoteList.as_view()),
    url(r'api/profile/profile-id/(?P<pk>[0-9]+)/$',views.ProfileList.as_view()),
    url(r'api/flashcards/flashcard-id/(?P<pk>[0-9]+)/$',views.flashcardList.as_view()),
    url(r'api/notes/notes-id/(?P<pk>[0-9]+)/$',views.ProfileList.as_view())...
]
