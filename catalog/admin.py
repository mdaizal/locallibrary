from django.contrib import admin
from .models import Author, Book, BookInstance, Genre, Language

# Register your models here.
# admin.site.register(Author)
# admin.site.register(Book)
# admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)

class BookInline(admin.TabularInline):
    '''Tabular Inline View of Book for Author detail view'''
    model = Book
    extra = 0

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    '''Admin View for Author'''
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

# Register Admin classes for Book and Book Instance using @register decorater instead of admin.site.register()
# for learning purpose
class BookInstanceInline(admin.TabularInline):
    '''Tabular Inline View of Book Instance for Book View'''
    model = BookInstance
    extra = 0 # to make sure no extra instance field generated
    classes = ['collapse'] # to make the field in collapse state with a 'show' button

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    '''Admin View for Book'''
    list_display = ('title', 'author', 'display_genre')
    fieldsets = (
        (None, {
            'fields': (
                'title', 'author', 'summary', 'isbn'
            ),
        }),
        ('GENRES AND LANGUAGES', {
            'classes': ('collapse',),
            'fields': ('genre', 'language'),
        }),
    )
    inlines = [BookInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    '''Admin View for BookInstance'''
    list_display = ('book', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': (
                'book', 'imprint', 'id'
            ),
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )