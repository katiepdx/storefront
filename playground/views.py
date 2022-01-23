from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
  # return render --  with the request, a template name, and values to pass to the template as a dictionary object
  return render(request, 'hello.html', { 'name': 'Katie'})
