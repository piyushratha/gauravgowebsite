from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=15, null=True)
    emailid = models.CharField(max_length=100, null=True)
    subject = models.CharField(max_length=100, null=True)
    message = models.FileField(max_length=200, null=True)
    mdate = models.DateField(null=True)
    isread = models.CharField(max_length=10, null=True)
    def __str__(self):
        return self.name
    
    
class Games(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=5000, null=True)
    logo = models.FileField(null=True)
    image = models.FileField(null=True)
    creationdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title