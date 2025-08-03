from django.contrib import admin
from django.urls import path
from .views import books_list, books_detail
from .apps import LibraryConfig

app_name = LibraryConfig.name

urlpatterns = [
    path('books_list/', books_list, name='books_list'),
    path('books_detail/<int:book_id>', books_detail, name='books_detail'),
]
