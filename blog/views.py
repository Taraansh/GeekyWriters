from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Home")


def blog(request):
    return HttpResponse("This is blog")


def blogpost(request, slug):
    return HttpResponse(f"you are viewing {slug}")


def contact(request):
    return HttpResponse("This is contact page")