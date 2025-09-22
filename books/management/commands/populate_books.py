from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date
from books.models import Book

class Command(BaseCommand):
    help = 'Populate the database with sample books'

    def handle(self, *args, **options):
        sample_books = [
            {
                'title': 'The Great Gatsby',
                'author': 'F. Scott Fitzgerald',
                'isbn': '9780743273565',
                'publication_date': date(1925, 4, 10),
                'description': 'A classic American novel set in the Jazz Age, following the mysterious Jay Gatsby and his obsession with the beautiful Daisy Buchanan.',
                'genre': 'fiction',
                'price': 12.99
            },
            {
                'title': 'To Kill a Mockingbird',
                'author': 'Harper Lee',
                'isbn': '9780061120084',
                'publication_date': date(1960, 7, 11),
                'description': 'A gripping tale of racial injustice and childhood innocence in the American South during the 1930s.',
                'genre': 'fiction',
                'price': 14.99
            },
            {
                'title': '1984',
                'author': 'George Orwell',
                'isbn': '9780451524935',
                'publication_date': date(1949, 6, 8),
                'description': 'A dystopian social science fiction novel about totalitarian control and surveillance.',
                'genre': 'sci_fi',
                'price': 13.99
            },
            {
                'title': 'Pride and Prejudice',
                'author': 'Jane Austen',
                'isbn': '9780141439518',
                'publication_date': date(1813, 1, 28),
                'description': 'A romantic novel of manners that critiques the British landed gentry of the early 19th century.',
                'genre': 'romance',
                'price': 11.99
            },
            {
                'title': 'The Catcher in the Rye',
                'author': 'J.D. Salinger',
                'isbn': '9780316769174',
                'publication_date': date(1951, 7, 16),
                'description': 'A coming-of-age story following teenager Holden Caulfield as he navigates the complexities of adolescence.',
                'genre': 'young_adult',
                'price': 13.49
            },
            {
                'title': 'The Hobbit',
                'author': 'J.R.R. Tolkien',
                'isbn': '9780547928227',
                'publication_date': date(1937, 9, 21),
                'description': 'A fantasy novel about a hobbit who goes on an unexpected journey to help dwarves reclaim their homeland.',
                'genre': 'fantasy',
                'price': 15.99
            },
            {
                'title': 'The Da Vinci Code',
                'author': 'Dan Brown',
                'isbn': '9780307474278',
                'publication_date': date(2003, 3, 18),
                'description': 'A mystery thriller that follows symbologist Robert Langdon as he investigates a murder in the Louvre.',
                'genre': 'mystery',
                'price': 16.99
            },
            {
                'title': 'The Alchemist',
                'author': 'Paulo Coelho',
                'isbn': '9780061122415',
                'publication_date': date(1988, 1, 1),
                'description': 'A philosophical novel about a young Andalusian shepherd who travels from Spain to Egypt in search of treasure.',
                'genre': 'fiction',
                'price': 14.49
            },
            {
                'title': 'Sapiens',
                'author': 'Yuval Noah Harari',
                'isbn': '9780062316097',
                'publication_date': date(2011, 1, 1),
                'description': 'A brief history of humankind, exploring how Homo sapiens came to dominate the world.',
                'genre': 'history',
                'price': 18.99
            },
            {
                'title': 'Atomic Habits',
                'author': 'James Clear',
                'isbn': '9780735211292',
                'publication_date': date(2018, 10, 16),
                'description': 'A guide to building good habits and breaking bad ones through small, incremental changes.',
                'genre': 'self_help',
                'price': 17.99
            }
        ]

        created_count = 0
        for book_data in sample_books:
            book, created = Book.objects.get_or_create(
                isbn=book_data['isbn'],
                defaults=book_data
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created: {book.title} by {book.author}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Already exists: {book.title} by {book.author}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'\nSuccessfully created {created_count} new books!')
        )
        self.stdout.write(
            self.style.SUCCESS(f'Total books in database: {Book.objects.count()}')
        )
