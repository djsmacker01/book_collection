from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'price', 'publication_date', 'created_at')
    list_filter = ('genre', 'publication_date', 'created_at')
    search_fields = ('title', 'author', 'isbn')
    list_editable = ('price',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'author', 'isbn')
        }),
        ('Details', {
            'fields': ('publication_date', 'genre', 'price', 'description')
        }),
        ('Cover Image', {
            'fields': ('cover_image',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
