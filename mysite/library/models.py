from django.db import models
from django.shortcuts import reverse
from django.core.exceptions import ValidationError
from django.core import validators
from django.core.validators import MinLengthValidator,  RegexValidator
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100, validators=[MinLengthValidator(limit_value=3, message=">3")])
    birth_date = models.DateField("date published")
    digit_field = models.CharField(max_length=10, default=0, validators=[
        validators.RegexValidator(regex=r'^[-+]?([1-9]\d*|0)$', message='Only digits')])
    def __str__(self):
        return f'ID: {self.pk}, {self.name}, {self.digit_field}'

    # def get_absolute_url(self):
    #     return f'author/{self.name}/'
    #     # return reverse('index', kwargs={'name': self.name})


class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateField("date published")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    def __str__(self):
        return self.first_name

class BookInstance(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    imprint = models.CharField(max_length=100)
    due_back = models.DateField("date published")
    status = models.CharField(max_length=100)
    borrower = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.imprint

class Genre(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)
    def __str__(self):
        return self.name


