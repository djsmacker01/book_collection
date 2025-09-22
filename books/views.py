from django.shortcuts import render, get_object_or_404
from .models import Book

def home(request):
    """Home page view"""
    books = Book.objects.all()[:6]  # Show first 6 books
    return render(request, 'books/home.html', {'books': books})

def book_list(request):
    """List all books"""
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, book_id):
    """Display detailed information about a specific book"""
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'books/book_detail.html', {'book': book})
