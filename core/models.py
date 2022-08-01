from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models

from order.models import Order

class User(AbstractUser):
    email = models.EmailField(unique=True)

    def accessContent(self, obj_id, obj_type):
        return UserAccessContent.objects.filter(
                                    content_type=obj_type, 
                                    object_id=obj_id,
                                    user_id=self.id).exists()

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='user/images', null=True)

    def __str__(self):
        return self.user.email


class UserAccessContent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
