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


def catelogue(request):
    return render(request, 'catelogue.html')


def commercial_design(request):
    return render(request, 'commercial-design.html')


def residential_design(request):
    return render(request, 'residential-design.html')


def restaurant_design(request):
    return render(request, 'restaurant-design.html')


def industrial_design(request):
    return render(request, 'industrial-design.html')


def corporate_design(request):
    return render(request, 'corporate-design.html')


def hospitality_design(request):
    return render(request, 'hospitality-design.html')
