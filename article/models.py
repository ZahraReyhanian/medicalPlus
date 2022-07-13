from email.policy import default
from django.conf import settings
from django.db import models
from django.template.defaultfilters import truncatechars
from tinymce.models import HTMLField
from jalali_date import datetime2jalali
import re

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

    class Meta:
        get_latest_by = ['updated_at']

    def __str__(self) -> str:
        return self.title

    @property
    def short_body(self):
        text = re.sub('<[^<]+?>|\r|\n|&[a-zA-Z;]*', '', self.body)
        return truncatechars(text, 100)

    def get_jalali_created_at(self):
        return datetime2jalali(self.created_at).strftime('%Y/%m/%dd')

    def get_jalali_updated_at(self):
        return datetime2jalali(self.updated_at).strftime('%Y/%m/%dd')

class SaveArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    class Meta:
        unique_together = [['article', 'user']]
