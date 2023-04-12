from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def services(request):
    return render(request, 'services.html')


def About(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def projects(request):
    return render(request, 'projects.html')
