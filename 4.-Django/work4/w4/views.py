from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "h4/index.html")
    
def sec(request):
    return HttpResponse("Hello, Second!!")

def third(request):
    return HttpResponse("Hello, Third!!")



def greet(request, name):
    return render(request, "h4/greet.html", {
        "name": name.capitalize()
    })
    
