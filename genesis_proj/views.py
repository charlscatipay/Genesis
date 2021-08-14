from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django import template


# Create your views here.

def homepage(request):
    # return HttpResponse('Homepage')
    return render(request, 'index.html')
