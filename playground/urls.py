from django.urls import path
from . import views

# URLConf module - url configuration
# list of url pattern objects
# django looks for urlpatterns list
urlpatterns = [
  path('hello/', views.say_hello)
]
