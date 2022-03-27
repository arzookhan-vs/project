from django.db import models

# Create your models here.
class Demo(models.Model):
  email = models.CharField(max_length=121)
  text = models.TextField()
  result = models.TextField()
  date = models.DateField()
  
  def __str__(self):
    return self.email
