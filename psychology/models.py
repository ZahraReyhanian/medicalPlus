from django.db import models

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
    description = models.TextField()
    questions = models.IntegerField()
    type = models.CharField(
        max_length=5, choices=TYPE_CHOICES
    )
    price = models.CharField(max_length=255)
    answers = models.TextField(null=True)
    image = models.TextField(null=True)
    tags = models.CharField(max_length=255)
    viewCount = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


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
    answers = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# class TestUserStatus(models.Model):
#     test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='user_status')
#     #user_id
#     #status
#     result = models.TextField(null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class TestUserAnswer(models.Model):
#     question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE, related_name='user_answers')
#     user_choice = models.PositiveIntegerField()
#     #user_id
#     created_at = models.DateTimeField(auto_now_add=True)



