"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from myapp import views  # Make sure this is correct

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Include myapp URLs
    path('', views.home_view, name='home'),  # Update this line
    path('contact/', views.contact_view, name='contact'),
    path('success/', views.success_view, name='success'),
    path('about/', views.about_view, name='about'),
]
