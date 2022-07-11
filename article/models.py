from email.policy import default
from django.conf import settings
from django.db import models
from tinymce.models import HTMLField

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    lang = models.CharField(max_length=10, default='fa')
    body = HTMLField(blank=True)
    image = models.ImageField(upload_to='article/images', null=True)
    viewCount = models.IntegerField(default=0)
    commentCount = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)