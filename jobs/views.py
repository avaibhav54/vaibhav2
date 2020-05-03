from django.shortcuts import render
from django.http import HttpResponse
from .models import job
def home(request):
    jobs=job.objects
    return render(request,'jobs/home.html',{'jobs':jobs})
