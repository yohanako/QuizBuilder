from django.db import models

class Questions(models.Model):
    question = models.CharField(max_length=100)

    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    
    answer = models.CharField(max_length=200)

class Answer(models.Model):
    correct = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)