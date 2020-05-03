from django.shortcuts import render
from django.http import HttpResponse
from .models import job
def home(request):
    jobs=job.objects
    ms='vaibhav ag'
    return render(request,'home.html',{'jobs':jobs,'namere':ms})
