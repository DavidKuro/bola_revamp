from django.db import models
from django.db.models import Model
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True,null=True,unique=False)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = RichTextField(blank=True,null=True,unique=False)  
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=True)
    cover_image_url = models.URLField(max_length=200, blank=True)
    blockquote = models.CharField(max_length=150, blank=True,null=True)
    # slug = AutoSlugField(populate_from='title')

   
    
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('bola:detail-page', kwargs={'pk': self.pk,})

