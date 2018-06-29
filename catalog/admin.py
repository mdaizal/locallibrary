from django.contrib import admin
from .models import Author, Book, BookInstance, Genre, Language

# Register your models here.
# admin.site.register(Author)
# admin.site.register(Book)
# admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    '''Admin View for Author'''
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

# Register Admin classes for Book and Book Instance using @register decorater instead of admin.site.register()
# for learning purpose
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    '''Admin View for Book'''
    list_display = ('title', 'author', 'display_genre')

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    '''Admin View for BookInstance'''
    list_filter = ('status', 'due_back')