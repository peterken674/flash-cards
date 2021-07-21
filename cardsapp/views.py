from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Profile, FlashCard, Note
from .serializer import ProfileSerializer, FlashcardSerializer, NoteSerializer

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)

class FlashcardList(APIView):
    def get(self, request, format=None):
        all_flashcards = FlashCard.objects.all()
        serializers = ProfileSerializer(all_flashcards, many=True)
        return Response(serializers.data)

class NoteList(APIView):
    def get(self, request, format=None):
        all_notes = Note.objects.all()
        serializers = ProfileSerializer(all_notes, many=True)
        return Response(serializers.data)
