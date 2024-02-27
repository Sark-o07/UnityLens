from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from tinymce.models import HTMLField
# Create your models here.

class CategoryModel(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('blog-index')

class PostModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    intro = models.TextField(max_length=255)
    content = RichTextUploadingField()
    # content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, default='culture')
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True, default='thumbnail1.png')
    thumbnail = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ('-date_created',)
    
    def comment_count(self):
        return self.comments.all().count()
    
    def comment(self):
        return self.comments.all()

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)

    def __str__(self):
        return(self.content)