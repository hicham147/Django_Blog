from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

def home(request):
    context = Post.objects.all()
    return render(request,'home.html',{"Post":context})

def about(request):
    return render(request,'About.html')

def contect(request):
    return render(request,'register1.html')