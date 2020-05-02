from django.shortcuts import render
from .models import Blog
def allblogs(request):
    blogs=Blog.objects
    return render(request,'allblogs.html',{'blogs':blogs})
# Create your views here.
