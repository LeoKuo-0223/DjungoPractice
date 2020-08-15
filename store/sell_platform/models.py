from django.db import models

# Create your models here.
class SellPlatform(models.Model):
    Name = models.CharField(unique=True, max_length=50, verbose_name='Name')
    Description = models.TextField(verbose_name='Description')
    EditTime= models.DateTimeField(auto_now=True, verbose_name='Edit Time')