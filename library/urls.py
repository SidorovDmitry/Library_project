from django.contrib import admin
from django.urls import path
# from .views import books_list, books_detail
from .apps import LibraryConfig
from .views import BooksListView, BooksCreateView, BooksUpdateView, BooksDetailView, BooksDeleteView

app_name = LibraryConfig.name

urlpatterns = [
    path('books/', BooksListView.as_view(), name='books_list'),
    path('books/new/', BooksCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/', BooksDetailView.as_view(), name='book_detail'),
    path('books/update/<int:pk>/', BooksUpdateView.as_view(), name='book_update'),
    path('books/delete/<int:pk>/', BooksDeleteView.as_view(), name='book_delete'),

    # path('books_list/', books_list, name='books_list'),
    # path('books_detail/<int:book_id>', books_detail, name='books_detail'),
]
