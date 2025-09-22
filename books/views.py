from django.shortcuts import render
from .models import Book

def home(request):
    """Home page view"""
    books = Book.objects.all()[:6]  # Show first 6 books
    return render(request, 'books/home.html', {'books': books})
