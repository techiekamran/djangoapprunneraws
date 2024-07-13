from django.shortcuts import render
from bookapp.models import Book
from django.views.generic.list import ListView
# Create your views here.

class BookView(ListView):
    model = Book
    template_name = 'book-list.html'
    context_object_name = 'books_list'
