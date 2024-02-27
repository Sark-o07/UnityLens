from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='flower.png', upload_to='profile', validators=[
                              FileExtensionValidator(['png', 'jpg', 'jpeg', 'webp'])])
    
    first_name = models.CharField(blank=True, null=True, max_length=100)
    last_name =  models.CharField(blank=True, null=True, max_length=100)
    profile_bio = models.CharField(blank=True, null=True, max_length=200)
    website_link = models.CharField(blank=True, null=True, max_length=200)
    medium_link = models.CharField(blank=True, null=True, max_length=200)
    reddit_link = models.CharField(blank=True, null=True, max_length=200)
    quora_link = models.CharField(blank=True, null=True, max_length=200)
    pinterest_link = models.CharField(blank=True, null=True, max_length=200)
    
    
    
    def __str__(self):
        return self.user.username

# Create your models here.
