from django.db import models

# Create your models here.

class developer(models.Model):
    username = models.CharField(max_length=20)
    bio = models.TextField(null=True,blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username