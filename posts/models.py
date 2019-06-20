from django.db import models
from datetime import datetime



MINISTRY = [
    ('AGRIC AND LIVESTOCK', 'Agriculture And Livestock'),
    ('ENVIRON AND NATURAL RESOURCES', 'Environment And Natural Resources'),
    ('FINANCE AND ECONOMIC PLANNING', 'Finance And Economic Planning'),
    ('HEALTH AND SANITATION', 'Health And Sanitaion'),
    ('PHYSICAL PLANNING AND URBAN DEVELOPMENT', 'Physical Planning And Urban Development'),
    ('ROAD TRANSPORT AND PUBLIC WORKS', 'Road Transport And Public Works'),
    ('FINANCE AND ECONOMIC PLANNING', 'Finance And Economic Planning'),
    ('TOURISM ARTS CULTURE AND SPORT', 'Tourism Arts Culture And Sport.'),
    ('BUSINESS COOPERATIVES AND MARKETING', 'Business Cooperatives And Marketing'),
]

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


class Projects(models.Model):
  title = models.CharField(max_length=200)
  body = models.TextField()
  created_at = models.DateTimeField(default=datetime.now, blank=True)
  images = models.ImageField( upload_to='images/')
  author = models.CharField(max_length = 200, default='')

  def __str__(self):
    return self.title

    
  class Meta:
    verbose_name_plural = "Projects"


class Comment(models.Model):
    post = models.ForeignKey('posts.Projects', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=datetime.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text







  
