from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings

class Order(models.Model):
    STATUS_NOTSTART = '1'
    STATUS_FAILED = '2'
    STATUS_ERROR = '3'
    STATUS_BLOCKED = '4'
    STATUS_RETURNP = '5'
    STATUS_RETURNS = '6'
    STATUS_CANCELED = '7'
    STATUS_TRANSFERED = '8'
    STATUS_WAITING = '10'
    STATUS_CONFIRMED = '100'

    STATUS_CHOICES = [
        (STATUS_NOTSTART, 'not started'),
        (STATUS_FAILED, 'failed'),
        (STATUS_ERROR, 'error'),
        (STATUS_BLOCKED, 'blocked'),
        (STATUS_RETURNP, 'returned to payer'),
        (STATUS_RETURNS, 'systemic returned'),
        (STATUS_CANCELED, 'canceled'),
        (STATUS_TRANSFERED, 'tranfered to gateway'),
        (STATUS_WAITING, 'waiting to accept'),
        (STATUS_CONFIRMED, 'confirmed'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=5, choices=STATUS_CHOICES, default=STATUS_NOTSTART
    )
    track_id = models.CharField(max_length=100, null=True)
    refID = models.CharField(max_length=100, null=True)
    link = models.CharField(max_length=200, null=True)
    amount = models.CharField(max_length=255)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
