from django.shortcuts import render
from django.http import HttpResponse

from .models import Posts


def index(request):
 

  posts = Posts.objects.all().order_by('-created_at')[:3]

  context = {
    'title': 'Stay Updated',
    'posts': posts
  }

  return render(request, 'posts/index.html', context)

def details(request, id):
  post = Posts.objects.get(id=id)

  context = {
    'post': post
  }

  return render(request, 'posts/details.html', context)