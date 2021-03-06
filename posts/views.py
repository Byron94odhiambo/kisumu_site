from django.shortcuts import render, redirect, get_object_or_404
from .models import Posts, Adverts,Projects
from .forms import ContactForm, MinistryForm,CommentForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.db.models import Q



def index(request):
 

  posts = Posts.objects.all().order_by('-created_at')[:3]

  context = {
    'title': 'Latest Posts',
    'posts': posts
  }

  return render(request, 'posts/index.html', context)

def details(request, id):

  post = Posts.objects.get(id=id)

  context = {
    'post': post
  }

  return render(request, 'posts/details.html', context)


def contact(request):

  if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email code goes here
            sender_name = form.cleaned_data['first_name']
            sender_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            
            message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
            send_mail(subject, message, sender_email, ['odhiambobyron39@gmail.com'])
            
  else:
        form = ContactForm()
   

  return render(request, 'posts/contact.html', {'form': form,})

  
def news(request):
 

  posts = Posts.objects.all().order_by('-created_at')

  context = {
    'title': 'news/events',
    'posts': posts
  }

  return render(request, 'posts/news.html', context)


def tenders(request):
 

     adverts = Adverts.objects.all().order_by('-ad_created_at')

     context = {
           'title': 'STAY UPDATED',
           'adverts': adverts
           }

     return render(request, 'posts/tenders.html', context)


def services(request):

  return render(request, 'posts/services.html')


def ministries(request):
  if request.method == 'POST':
        form = MinistryForm(request.POST)
        if form.is_valid():
            # send email code goes here
            ministry=form.cleaned_data['ministry']
            sender_name = form.cleaned_data['first_name']
            sender_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            
            message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
            send_mail(ministry,subject, message, sender_email, ['odhiambobyron39@gmail.com'])
            
  else:
        form = MinistryForm()
   

  return render(request, 'posts/ministries.html', {'form': form,})



def projects(request):
   projects = Projects.objects.all().order_by('-created_at')[:3]

   context = {
    'title': 'Latest Projects',
    'projects': projects
   }
     
   return render(request, 'posts/projects.html', context)

def review(request, id):

  project = Projects.objects.get(id=id)

  context = {
    'project': project
  }

  return render(request, 'posts/review.html', context)


def add_comment_to_project(request, id):
    project = get_object_or_404(Projects, id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.project = project
            comment.save()
            return redirect('review', id=project.id)
    else:
        form = CommentForm()
    return render(request, 'posts/add_comment_to_project.html', {'form': form})

def objectives(request):
    return render (request, 'posts/objectives.html')

def about_us(request):
    return render(request,'posts/about_us.html')



