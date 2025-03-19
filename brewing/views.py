from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to Brewing</h1><p>This is the brewing app!</p>")
