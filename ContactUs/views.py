from django.shortcuts import render

def ContactUs(request):
    return render(request, "ContactUs/contact.html")


def Contact2(request):
    return render(request, "ContactUs/contact2.html")