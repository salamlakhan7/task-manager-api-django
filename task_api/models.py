from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    STATUS_CHOICES = [('pending', 'Pending'), ('completed', 'Completed')]
    completed = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
