from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('success/', views.success_view, name='success'),
    path('about/', views.about_view, name='about'),
]
