from django.shortcuts import render
from .models import Book

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class BooksListView(ListView):
    model = Book
    template_name = 'library/books_list.html'
    context_object_name = 'books'

class BooksCreateView(CreateView):
    model = Book
    fields = ['title', 'publication_date', 'author']
    template_name = 'library/book_forms.html'
    success_url = reverse_lazy('library:books_list')


class BooksDetailView(DetailView):
    model = Book
    template_name = 'library/book_detail.html'
    context_object_name = 'books'


class BooksUpdateView(UpdateView):
    model = Book
    fields = ['title', 'publication_date', 'author']
    template_name = 'library/book_forms.html'
    success_url = reverse_lazy('library:books_list')


class BooksDeleteView(DeleteView):
    model = Book
    template_name = 'library/book_confirm_delete.html'
    success_url = reverse_lazy('library:books_list')

# def books_list(request):
#     books = Book.objects.all()
#     context = {'books': books}
#     return render(request,'library/books_list.html', context=context)
#
#
# def books_detail(request, book_id):
#     book = Book.objects.get(id=book_id)
#     context = {'book': book}
#     return render(request,'library/books_detail.html', context=context)