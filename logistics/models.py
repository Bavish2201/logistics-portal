from django.db import models

# Create your models here.

class Logistic(models.Model):

    ITEM_CHOICES = (
        ('chair', 'Chair'),
        ('table', 'Table')
    ) 

    To = models.CharField(max_length=200)
    From = models.CharField(max_length=200)
    Timestamp = models.DateTimeField()
    Item = models.CharField(choices=ITEM_CHOICES, max_length=20)
    Purpose = models.TextField()