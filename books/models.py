from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
import os

def book_cover_upload_path(instance, filename):
    """Generate file path for book cover images"""
    return f'book_covers/{instance.isbn}/{filename}'

class Book(models.Model):
    GENRE_CHOICES = [
        ('fiction', 'Fiction'),
        ('non_fiction', 'Non-Fiction'),
        ('mystery', 'Mystery'),
        ('romance', 'Romance'),
        ('sci_fi', 'Science Fiction'),
        ('fantasy', 'Fantasy'),
        ('biography', 'Biography'),
        ('history', 'History'),
        ('self_help', 'Self Help'),
        ('business', 'Business'),
        ('poetry', 'Poetry'),
        ('drama', 'Drama'),
        ('horror', 'Horror'),
        ('thriller', 'Thriller'),
        ('young_adult', 'Young Adult'),
        ('children', 'Children'),
        ('other', 'Other'),
    ]
    

    title = models.CharField(
        max_length=200,
        help_text="Enter the book title"
    )
    
    author = models.CharField(
        max_length=200,
        help_text="Enter the author's name"
    )
    
    isbn = models.CharField(
        max_length=17, 
        unique=True,
        help_text="13 or 10 digit ISBN number"
    )
    
    publication_date = models.DateField(
        help_text="Date when the book was published"
    )
    
    
    description = models.TextField(
        max_length=2000,
        help_text="Brief description of the book",
        blank=True
    )
    
    genre = models.CharField(
        max_length=20,
        choices=GENRE_CHOICES,
        default='other',
        help_text="Select the book genre"
    )
    
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
        help_text="Price in USD"
    )
    
    
    cover_image = models.ImageField(
        upload_to=book_cover_upload_path,
        blank=True,
        null=True,
        help_text="Upload book cover image"
    )
    
   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['title']
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('book_detail', args=[str(self.id)])
    
    def get_cover_url(self):
        """Returns the URL for the book cover image or a default image."""
        if self.cover_image and hasattr(self.cover_image, 'url'):
            return self.cover_image.url
        return '/static/images/default-book-cover.jpg'
    
    def get_genre_display_name(self):
        """Returns the human-readable genre name."""
        return dict(self.GENRE_CHOICES).get(self.genre, self.genre)
    
    def formatted_price(self):
        """Returns the price formatted as currency."""
        return f"${self.price:.2f}"