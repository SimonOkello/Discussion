from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    """
    This is the homepage route
    """
    return HttpResponse("We have launched out discussion app")