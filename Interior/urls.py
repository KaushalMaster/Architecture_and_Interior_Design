from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services', views.services, name='services'),
    path('About', views.About, name='About'),
    path('contact', views.contact, name='contact'),
    path('projects', views.projects, name='projects')
]
