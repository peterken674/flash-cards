from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Profile, FlashCard, Note
from .serializer import ProfileSerializer, FlashcardSerializer, NoteSerializer


class ProfileList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        profile = self.get_profile(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FlashcardList(APIView):
    def get(self, request, format=None):
        all_flashcards = FlashCard.objects.all()
        serializers = ProfileSerializer(all_flashcards, many=True)
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = FlashcardSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        flashcard = self.get_flashcard(pk)
        serializers = FlashcardSerializer(flashcard, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        flashcard = self.get_flashcard(pk)
        flashcard.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NoteList(APIView):
    def get(self, request, format=None):
        all_notes = Note.objects.all()
        serializers = ProfileSerializer(all_notes, many=True)
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = NoteSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        note = self.get_note(pk)
        serializers = NoteSerializer(note, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        note = self.get_note(pk)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)