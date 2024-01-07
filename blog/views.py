from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Blog, Contact
import math

# Create your views here.


def home(request):
    return render(request, 'index.html')


def blog(request):
    no_of_posts = 7
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)

    blogs = Blog.objects.all()
    length = len(blogs)
    blogs = Blog.objects.all()[(page - 1) * no_of_posts: page * no_of_posts]

    if page > 1:
        prev = page - 1
    else:
        prev = None

    if page < math.ceil(length/no_of_posts):
        nxt = page + 1
    else:
        nxt = None

    context = {'blogs': blogs, 'prev': prev, 'nxt': nxt}
    return render(request, 'bloghome.html', context)


def blogpost(request, slug):
    blog = Blog.objects.filter(slug=slug).first()
    context = {'blog': blog}
    return render(request, 'blogpost.html', context)


def search(request):
    return render(request, 'search.html')


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        ins = Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
        print("written to database")
    return render(request, 'contact.html')


def addblog(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        short_desc = request.POST['short_desc']
        desc = short_desc.split()
        slug = '-'.join(desc)
        blog = Blog(title=title, content=content,
                    short_desc=short_desc, slug=slug)
        blog.save()
        print('blog is saved')
        return redirect('/blog/')
    return render(request, 'addblog.html')
