import re
from django.template.defaultfilters import truncatechars
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Test(models.Model):
    TYPE_FREE = 'free'
    TYPE_CASH = 'cash'

    TYPE_CHOICES = [
        (TYPE_FREE, 'free'),
        (TYPE_CASH, 'cash'),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50, allow_unicode=True)
    body = HTMLField(blank=True)
    questions = models.IntegerField()
    type = models.CharField(
        max_length=5, choices=TYPE_CHOICES
    )
    time = models.IntegerField(default=3)
    price = models.CharField(max_length=255, default=0)
    answers = models.JSONField(null=True, blank=True)
    image = models.ImageField(upload_to='psychology/images/tests', null=True)
    tags = models.CharField(max_length=255)
    viewCount = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self) -> str:
        return self.title

    @property
    def description(self):
        text = re.sub('<[^<]+?>|\r|\n|&[a-zA-Z;]*', '', self.body)
        return truncatechars(text, 100)

    @property
    def contentType(self):
        test_type = ContentType.objects.filter(app_label='psychology', model='test').get();
        return test_type.id

    #todo change when deploy
    @property
    def redirectLink(self):
        return f'http://localhost:3000/tests/{self.id}/questions'


class TestResult(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='testresults')
    result = models.TextField()
    grade = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class TestQuestion(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='testquestions')
    number = models.PositiveIntegerField()
    question = models.TextField()
    numberOfAnswer = models.PositiveIntegerField()
    answers = models.JSONField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class TestUserStatus(models.Model):
    STATUS_NOTSTART = 'N'
    STATUS_GETSTART = 'G'
    STATUS_SUBMITTED = 'S'

    STATUS_CHOICES = [
        (STATUS_NOTSTART, 'not started'),
        (STATUS_GETSTART, 'get strated'),
        (STATUS_SUBMITTED, 'submitted'),
    ]
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='user_status')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=5, choices=STATUS_CHOICES, default=STATUS_NOTSTART
    )
    result = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)




