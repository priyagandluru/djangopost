from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

# Create your views here.

def index(request):
    post = Post.objects.all()
    
    #print(post)
    return render(request,'index.html',context={'posts':post})
def about(request):
    return render(request,'about.html')