from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    summary = models.TextField(max_length=1000)