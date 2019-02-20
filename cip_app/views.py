from django.shortcuts import render

# Create your views here.
import re
from datetime import datetime

# Replace the existing home function with the one below
def home(request):
    return render(request, "cip_app/home.html")

def about(request):
    return render(request, "cip_app/about.html")

def contact(request):
    return render(request, "cip_app/contact.html")

def hello_there(request, name):
    return render(
        request,
        'cip_app/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )