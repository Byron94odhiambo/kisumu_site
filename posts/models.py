from django.db import models
from datetime import datetime

class Posts(models.Model):
  title = models.CharField(max_length=200)
  body = models.TextField()
  created_at = models.DateTimeField(default=datetime.now, blank=True)
  images = models.ImageField( upload_to='images/')
  author = models.CharField(max_length = 200, default='')

  def __str__(self):
    return self.title

    
  class Meta:
    verbose_name_plural = "Posts"

class Adverts(models.Model):
  ad_title = models.CharField(max_length=200)
  ad_body = models.TextField()
  ad_created_at = models.DateTimeField(default=datetime.now, blank=True)

  def __str__(self):
    return self.ad_title
    
  class Meta:
    verbose_name_plural = "Adverts"  



  
