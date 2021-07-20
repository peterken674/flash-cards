from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=1000, blank=True)
    profile_pic = CloudinaryField('images', default='image/upload/v1626430054/default_zogkvr.png')
    grade = models.CharField(max_length=50)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    def __str__(self):
        return self.user.username

class FlashCard(models.Model):
    title = models.CharField(max_length=200)

    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='flashcards')

    def __str__(self):
        return self.title

class Note(models.Model):
    note = models.TextField()

    flashcard = models.ForeignKey(FlashCard, on_delete=models.CASCADE, related_name='notes')

