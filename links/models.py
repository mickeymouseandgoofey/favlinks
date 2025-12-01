from django.db import models
from django.contrib.auth.models import User

class Link(models.Model): #defines a link model
    user = models.ForeignKey(User, on_delete=models.CASCADE) #Each link is associated with a user.  If user is deleted, their links are also deleted.
    title = models.CharField(max_length=255) #Title of the link max length 255 characters
    url = models.URLField() #URL field to store the link
    description = models.TextField(blank=True) #Optional description field
    tags = models.CharField(max_length=255, blank=True) #Optional tags field
    created_at = models.DateTimeField(auto_now_add=True) #Timestamp when the link was created

    def __str__(self):
        return self.title
