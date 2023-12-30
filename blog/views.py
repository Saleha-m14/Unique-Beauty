from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def blogapp(request):
    return HttpResponse("Blog app")
