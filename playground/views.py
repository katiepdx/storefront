from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
  # return instance of the HttpResponse class 
  return HttpResponse('Hello world')
