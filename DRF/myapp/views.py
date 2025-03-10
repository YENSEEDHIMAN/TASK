from rest_framework import generics
from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer 

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

def login_view(request):
    return render(request, 'login.html')  
