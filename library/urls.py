from django.urls import path

from .apps import LibraryConfig
from .views import BooksListView, BookCreateView, BookUpdateView, BookDetailView, BookDeleteView, AuthorCreateView, AuthorUpdateView, AuthorListView, ReviewBookView, RecommendBookView

app_name = LibraryConfig.name

urlpatterns = [
    path('authors', AuthorListView.as_view(), name='authors_list'),
    path('author/new/', AuthorCreateView.as_view(), name='author_create'),
    path('author/update/<int:pk>/', AuthorUpdateView.as_view(), name='author_update'),
    path('books/', BooksListView.as_view(), name='books_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/new/', BookCreateView.as_view(), name='book_create'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),
    path('books/review/<int:pk>/', ReviewBookView.as_view(), name='book_review'),
    path('books/recommend/<int:pk>/', RecommendBookView.as_view(), name='book_recommend'),
]
