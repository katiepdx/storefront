from django.shortcuts import render
from django.http import HttpResponse

def calculate():
  x = 1
  y = 2
  return x # add 2nd debugger here

# Create your views here.
def say_hello(request):
  x = calculate() # add 1st debugger here
  
  # return render --  with the request, a template name, and values to pass to the template as a dictionary object
  return render(request, 'hello.html', { 'name': 'Katie'})
