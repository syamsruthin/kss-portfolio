from django.db import models

# Create blog models
class Blog(models.Model):
    title = models.CharField(max_length = 255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to= 'images/')

# Add the blog app to settings 


# create a migration


# Migrate


# Add to the admin
