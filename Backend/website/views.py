from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    context = {
        'response': "Backend response",
        "2_1": "2" + " x " + " 2 " + " = " + " 4",
        '2': "two",
        "3": "three",
        "4": "four"
    }
    print(context['2_1'])
    return render(request, 'website/index.html', context)


def About(request):
    return HttpResponse("Hello World")