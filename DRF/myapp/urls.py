from django.urls import path
from .views import BookListCreateView, BookDetailView, login_view  

urlpatterns = [
    path('', login_view, name='home'),  
    path('books/', BookListCreateView.as_view(), name='book-list'),
    path('books/<slug:pk>/', BookDetailView.as_view(), name='book-detail'),
]
