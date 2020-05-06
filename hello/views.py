from django.shortcuts import render
from django.http import HttpResponse

from .models import *

import requests

#~ # Create your views here.
#~ def index(request):
    #~ # return HttpResponse('Hello from Python!')
    #~ return render(request, "index.html")

def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

from django.template import loader, Context
from django.http import HttpResponse

def archive(request):
	posts = BlogPost.objects.all()
	t = loader.get_template("archive.html")
	c = { 'posts': posts }
	return HttpResponse(t.render(c))
