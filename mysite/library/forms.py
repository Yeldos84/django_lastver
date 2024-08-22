from django import forms
from django.forms import ModelForm
from .models import Author, Book, Publisher
from django.core.exceptions import ValidationError
from django.core import validators
class AuthorForm(forms.Form):
    name = forms.CharField(max_length=100)
    birth_date = forms.DateField()
    digit_field = forms.IntegerField()


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["title", "publication_date", "author"]

class PublisherForm(ModelForm):
    class Meta:
        model = Publisher
        fields = "__all__"
