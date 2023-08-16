from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView,
    )

# Create your views here.
def home (request):
    return render(request,'bola/home.html')

def blogpost (request):
    return render(request,'bola/blogpost.html')

def about (request):
    return render(request,'bola/about.html')

def properties (request):
    return render(request,'bola/properties.html')

def contact (request):
    return render(request,'bola/contact.html')

def blog (request):
    posts = Post.objects.all()
    return render(request,'bola/blog.html', {'posts': posts})

def detail_page (request, pk):
    post = Post.objects.get(pk=pk)
    return render (request,'bola/detail_page.html', {'post': post})

def page404 (request, exception):
    return render(request,'bola/page404.html', status=404)



