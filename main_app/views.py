from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def passwds_index(request):
    return render(request, 'passwds/index.html')