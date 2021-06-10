from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts, 'title': 'Home page'})


def about(request):
    return render(request, 'women/about.html', {'title': 'About'})


def forum(request):
    return HttpResponse('<h1>forummm</h1>')


def categories(request, catid):
    return HttpResponse(f"<h1>text2</h1><p>{catid}</p>")


def archive(request, year):
    return HttpResponse(f"<h1>text2</h1><p>{year}</p>")
