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
    # Additional details fields
    background_image = models.ImageField(upload_to='backgrounds/', null=True, blank=True)
    additional_description = models.TextField(null=True, blank=True)
    playstore_link = models.URLField(max_length=500, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    publisher = models.CharField(max_length=200, default='GauravGo Games')
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=5.0)
    file_size = models.CharField(max_length=50, default='31mb')
    platforms = models.CharField(max_length=200, default='Web, Android, iOS')
    youtube_link = models.URLField(null=True, blank=True)
    def __str__(self):
        return self.title
