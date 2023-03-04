from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')


def blog(request):
    return render(request, 'bloghome.html')

def blogpost(request, slug):
    return HttpResponse(f"you are viewing {slug}")


def search(request):
    return render(request, 'search.html')


def contact(request):
    return render(request, 'contact.html')