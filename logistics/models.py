from django.db import models
from django.utils import timezone

# Create your models here.

class Logistic(models.Model):

    ITEM_CHOICES = (
        ('chair', 'Chair'),
        ('table', 'Table')
    ) 

    To = models.CharField(max_length=200)
    From = models.CharField(max_length=200)
    Timestamp = models.DateTimeField(default=timezone.now)
    Item = models.CharField(choices=ITEM_CHOICES, default='chair', max_length=20)
    Purpose = models.TextField()