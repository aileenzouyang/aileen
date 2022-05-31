from django.db import models

# Create your models here.
class Destination(models.Model):   
    name = models.CharField(max_length=100)
    email = models.EmailField(default="aileenzouyang@gmail.com")
    message = models.TextField(default="no message")

