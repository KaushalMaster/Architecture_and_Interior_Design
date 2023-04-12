from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services', views.services, name='services'),
    path('About', views.About, name='About'),
    path('contact', views.contact, name='contact'),
    path('projects', views.projects, name='projects'),
    path('catelogue', views.catelogue, name='catelogue'),
    path('commercial_design', views.commercial_design, name='commercial_design'),
    path('industrial_design', views.industrial_design, name='industrial_design'),
    path('residential_design', views.residential_design, name='residential_design'),
    path('restaurant_design', views.restaurant_design, name='restaurant_design')
]
