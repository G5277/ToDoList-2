from django.db import models
from django.utils import timezone
# Models

class Item(models.Model):
    task = models.CharField(max_length  = 100)
    description = models.TextField()
    date = models.DateTimeField(default = timezone.now)


    def __str__(self):
        return self.task