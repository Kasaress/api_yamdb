from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

User = get_user_model()

class Genre(models.Model):
    """Жанры произведений."""
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Жанр'
        ordering = ('id',)

    def __str__(self):
        return self.name


class Category(models.Model):
    """Категории произведение."""
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Категория'
        ordering = ('id',)


class Title(models.Model):
    """Произведения."""
    name = models.CharField(max_length=150)
    year = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='titles',
        verbose_name='Категория',
        blank=True,
        null=True,
        help_text='Выберите категорию'
    )
    genre = models.ManyToManyField(
        Genre,
        through='GenreTitle',
        verbose_name='Жанр',
        help_text='Выберите жанр'
    )

    class Meta:
        verbose_name = 'Произведение'
        ordering = ('id',)

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    """Произведения-Жанры."""
    genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        blank=True,
        null=True)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.genre}{self.title}'


class Review(models.Model):
    """Отзывы."""
    text = models.TextField(max_length=3000)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    pub_date = models.DateTimeField(auto_now_add=True)
    title = models.ForeignKey(Title, on_delete=models.CASCADE, related_name='reviews')

    class Meta:
        verbose_name = 'Отзывы'
        ordering = ('id',)


class Comment(models.Model):
    """Комментарии."""
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = 'Комментарии'
        ordering = ('id',)
