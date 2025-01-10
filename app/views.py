
from django.shortcuts import render,redirect, get_object_or_404
# Create your views here.

def landing(request):

    
    return render(request, 'landing.html')
