from django.contrib import admin
from .models import Author, Book, Publisher, User, BookInstance, Genre
# Register your models here.
# admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(User)
admin.site.register(BookInstance)
# admin.site.register(Genre)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'birth_date', 'digit_field']
    search_fields = ['name']
    list_editable = ['digit_field']
    ordering = ['name']
    list_per_page = 5
    list_filter = ['name', 'birth_date']


admin.site.register(Author, AuthorAdmin)


class GenreAdmin(admin.ModelAdmin):
    filter_horizontal = ['books']


admin.site.register(Genre, GenreAdmin)
