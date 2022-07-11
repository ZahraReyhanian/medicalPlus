from django.conf import settings
from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Test(models.Model):
    TYPE_FREE = 'free'
    TYPE_CASH = 'cash'
    TYPE_VIP = 'vip'

    TYPE_CHOICES = [
        (TYPE_FREE, 'free'),
        (TYPE_CASH, 'cash'),
        (TYPE_VIP, 'vip'),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField()
    body = HTMLField(blank=True)
    description = models.TextField(null=True)
    questions = models.IntegerField()
    type = models.CharField(
        max_length=5, choices=TYPE_CHOICES
    )
    time = models.IntegerField(default=3)
    price = models.CharField(max_length=255)
    answers = models.JSONField(null=True)
    image = models.ImageField(upload_to='psychology/images/tests')
    tags = models.CharField(max_length=255)
    viewCount = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class TestResult(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='testresults')
    result = models.TextField()
    grade = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TestQuestion(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='testquestions')
    number = models.PositiveIntegerField()
    question = models.TextField()
    numberOfAnswer = models.PositiveIntegerField()
    answers = models.JSONField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class TestUserAnswer(models.Model):
    question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE, related_name='user_answers')
    user_choice = models.PositiveIntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)



