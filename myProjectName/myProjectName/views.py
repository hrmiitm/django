from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, World. You are at HRM world.")
    return render(request, 'home.html')

def about(request):
    return HttpResponse("You are at ABOUT PAGE.")

def contact(request):
    # return HttpResponse("You are at CONTACT PAGE.")
    return render(request, 'website/contact.html')