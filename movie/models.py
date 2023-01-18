from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from movie.utils import get_file_path_poster, get_file_path_video


# Категория
class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        help_text='Unique value for product page URL, created from name.',
        verbose_name='URL'
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        super(Category, self).save(*args, **kwargs)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Tag(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        help_text='Unique value for product page URL, created from name.',
        verbose_name='URL'
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        super(Tag, self).save(*args, **kwargs)

    class Meta:
        ordering = ('name',)
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


# Жанр
class Genre(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name='URL',
        help_text='URL'
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        super(Genre, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        db_table = 'genre'


# класс movie для хранения фильмов в базе данных
class Movie(models.Model):
    # добавление n-количества жанров
    genre = models.ManyToManyField(
        'Genre',
        verbose_name='Жанр',
        help_text='Жанр'
    )
    # добавление n-количества категорий
    category = models.ManyToManyField(
        'Category',
        verbose_name='Категория',
        help_text='Категория'
    )
    # добавление n-количества тегов
    tags = models.ManyToManyField(
        'Tag',
        verbose_name='Теги',
        help_text='Теги',
    )
    # название фильма
    title = models.CharField(
        max_length=250,
        verbose_name='Название',
        help_text='Название',
    )
    # описание фильма
    description = models.TextField(
        verbose_name='Описание',
        help_text='Описание',
    )
    slogan = models.CharField(
        max_length=250,
        verbose_name='Слоган',
        help_text='Слоган',
    )
    # дата выхода фильма
    release_date = models.DateField(
        verbose_name='Дата выхода',
        help_text='Дата выхода',
    )
    # рейтинг фильма
    rating = models.FloatField(
        verbose_name='Рейтинг',
        help_text='Рейтинг',
    )
    # ссылка на постер фильма
    poster = models.ImageField(
        upload_to=get_file_path_poster,
        verbose_name='Постер',
        help_text='Постер',
    )
    # ссылка на видео фильма
    video = models.FileField(
        upload_to=get_file_path_video,
        verbose_name='Видео',
        help_text='Видео',
    )
