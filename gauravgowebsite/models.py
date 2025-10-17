from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=15, null=True)
    emailid = models.CharField(max_length=100, null=True)
    company = models.CharField(max_length=150, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_resolved = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.name} — {self.email} ({self.created_at.date()})"
    
    
class Games(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=5000, null=True)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    # categorize games by type
    GAME_TYPE_CHOICES = [
        ('ftp', 'Free to Play Games'),
        ('br', 'Battle Royale Games'),
        ('fps', 'FPS Games'),
        ('rpg', 'RPG Games'),
        ('sim', 'Simulation Games'),
        ('other', 'Other'),
    ]
    game_type = models.CharField(max_length=20, choices=GAME_TYPE_CHOICES, default='other')
    creationdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
