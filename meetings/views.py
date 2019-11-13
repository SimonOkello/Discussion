from django.shortcuts import render
from .models import Meeting

# Create your views here.


def index(request):
    """
    This is the landingpage route
    """
    
    return render(request, 'index.html', {})

def home(request):
    """
    Homepage route
    """
    meetings = Meeting.objects.all()
    return render(request, 'home.html', {'meetings':meetings})


