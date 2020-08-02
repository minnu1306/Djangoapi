from django.db import models

class Article(models.Model):
  title= models.CharField(max_length = 100)
  author= models.CharField(max_length=100)
  email= models.EmailField(max_length=100)
  

  def __str__(self):
     return self.title

# Create your models here.
