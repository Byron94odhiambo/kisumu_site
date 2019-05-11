from django.shortcuts import render
from .models import Posts, Adverts
from .forms import ContactForm
from django.http import HttpResponseRedirect 
from django.core.mail import send_mail




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