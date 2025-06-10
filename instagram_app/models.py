from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts' )
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='posts_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
