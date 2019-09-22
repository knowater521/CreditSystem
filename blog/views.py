#coding=utf-8
from django.shortcuts import render
from blog.models import BlogsPost
from django.shortcuts import render_to_response

# Create your views here.
def index(request):
    posts = BlogsPost.objects.all()
    return render_to_response('index.html',{'posts':posts})
