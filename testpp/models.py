from django.db import models

# Create your models here.
class FormModel(models.Model):
    name = models.CharField(max_length = 80)
    age = models.IntegerField()
    address = models.TextField()
 
