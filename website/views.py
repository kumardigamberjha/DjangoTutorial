from django.shortcuts import render
from django.http import HttpResponse


def Index(request):
    # return HttpResponse("Hello World")
    return render(request, "website/index.html")


def About(request):
    return HttpResponse("About US")

