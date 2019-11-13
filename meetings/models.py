from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Meeting(models.Model):
    name=models.CharField(max_length=200, unique=True)
    description=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Question(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, related_name='questions')
    subject = models.CharField(max_length=200)
    last_updated = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return self.subject

class Reply(models.Model):
    message = models.TextField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at= models.DateTimeField(null=True)
    created_by= models.ForeignKey(User, on_delete=models.CASCADE, related_name='replies')
    updated_by=models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name= '+')

    def __str__(self):
        return self.message

