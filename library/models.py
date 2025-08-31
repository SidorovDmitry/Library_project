from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    birth_date = models.DateField(verbose_name='Дата рождения')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'
        ordering = ['last_name']


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название книги')
# Название книги. Строка максимальной длиной 200 символов.

    publication_date = models.DateField(verbose_name='Дата публикации')
#  Дата публикации книги. Поле для хранения даты.

    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
# Внешний ключ, связывающий книгу с автором. Указывает на модель Author и использует каскадное удаление
# on_delete=models.CASCADE. Это означает, что при удалении автора будут удалены и все связанные с ним книги.

    review = models.TextField(null=True, blank=True)

    redirect = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'
        ordering = ['title']
        permissions = [
            ("can_review_book", "Can review book"),
            ("can_recommend_book", "Can recommend book"),
        ]

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f'Review for {self.book.title}'