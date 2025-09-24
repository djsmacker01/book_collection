from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages
from .models import Book
from .forms import BookForm

def home(request):
    """Home page view"""
    books = Book.objects.all()[:6]  # Show first 6 books
    return render(request, 'books/home.html', {'books': books})

def book_list(request):
    """List all books with search and filtering"""
    books = Book.objects.all()
    search_query = request.GET.get('search', '')
    genre_filter = request.GET.get('genre', '')
    sort_by = request.GET.get('sort', 'title')
    
    # Search functionality
    if search_query:
        books = books.filter(
            Q(title__icontains=search_query) |
            Q(author__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    # Genre filtering
    if genre_filter:
        books = books.filter(genre=genre_filter)
    
    # Sorting
    if sort_by == 'title':
        books = books.order_by('title')
    elif sort_by == 'author':
        books = books.order_by('author')
    elif sort_by == 'price_low':
        books = books.order_by('price')
    elif sort_by == 'price_high':
        books = books.order_by('-price')
    elif sort_by == 'date_new':
        books = books.order_by('-publication_date')
    elif sort_by == 'date_old':
        books = books.order_by('publication_date')
    else:
        books = books.order_by('title')
    
    # Get unique genres for filter dropdown
    genres = Book.objects.values_list('genre', flat=True).distinct().order_by('genre')
    genre_choices = Book.GENRE_CHOICES
    
    context = {
        'books': books,
        'search_query': search_query,
        'genre_filter': genre_filter,
        'sort_by': sort_by,
        'genres': genres,
        'genre_choices': genre_choices,
    }
    return render(request, 'books/book_list.html', context)

def book_detail(request, book_id):
    """Display detailed information about a specific book"""
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'books/book_detail.html', {'book': book})

def add_book(request):
    """Add a new book"""
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            messages.success(request, f'Book "{book.title}" has been added successfully!')
            return redirect('book_detail', book_id=book.id)
    else:
        form = BookForm()
    
    return render(request, 'books/add_book.html', {'form': form})

def edit_book(request, book_id):
    """Edit an existing book"""
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save()
            messages.success(request, f'Book "{book.title}" has been updated successfully!')
            return redirect('book_detail', book_id=book.id)
    else:
        form = BookForm(instance=book)
    
    return render(request, 'books/edit_book.html', {'form': form, 'book': book})
