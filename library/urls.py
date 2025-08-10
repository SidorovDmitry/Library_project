from django.urls import path

from .apps import LibraryConfig
from .views import BooksListView, BookCreateView, BookUpdateView, BookDetailView, BookDeleteView

app_name = LibraryConfig.name

urlpatterns = [
    path('books/', BooksListView.as_view(), name='books_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/new/', BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/edit/', BookUpdateView.as_view(), name='book_edit'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
]
