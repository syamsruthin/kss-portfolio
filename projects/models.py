from django.db import models

# Create blog models
class Project(models.Model):
    image = models.ImageField(upload_to= 'images/')
    title = models.CharField(max_length = 255)    
    description = models.TextField()
    technologies = models.CharField(max_length = 300)
    

    def __str__(self):
        return self.title

    def project_description(self):
        return self.description[:100]
    
    
# Add the blog app to settings 


# create a migration


# Migrate


# Add to the admin
