from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("OK")

def login(request):
    if request.method == "POST":
        return HttpResponse("GOT POST REQUEST IN LOGIN ")
    else:
        return HttpResponse("GOT GET REQUEST IN LOGIN ")
