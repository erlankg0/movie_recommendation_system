from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from account.models import Gender, CustomUser
from movie.utils import get_file_path_poster, get_file_path_video


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


# класс актеров
class Actor(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )
    gender = models.ForeignKey(
        Gender,
        on_delete=models.PROTECT,
        verbose_name='Пол',
        help_text='Пол актера',
    )
    age = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='Возраст'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='actors/',
        verbose_name='Изображение'
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
        self.name = self.name.capitalize()
        super(Actor, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Актер'
        verbose_name_plural = 'Актеры'
        db_table = 'actor'


# класс режиссеров
class Director(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )
    gender = models.ForeignKey(
        Gender,
        on_delete=models.PROTECT,
        verbose_name='Пол',
        help_text='Пол актера',
    )
    age = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='Возраст'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='actors/',
        verbose_name='Изображение'
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
        self.name = self.name.capitalize()
        super(Director, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Режиссер'
        verbose_name_plural = 'Режиссеры'
        db_table = 'director'


# класс стран
class Country(models.Model):
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
        super(Country, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'
        db_table = 'country'


# класс комментариев
class Comment(MPTTModel):
    user = models.ForeignKey(
        'account.CustomUser',
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    movie = models.ForeignKey(
        'Movie',
        on_delete=models.CASCADE,
        verbose_name='Фильм'
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name='Родитель'
    )
    text = models.TextField(
        verbose_name='Текст'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )

    def __str__(self):
        return f'Комментарий {self.user} к {self.movie}'

    class MPTTMeta:
        order_insertion_by = ['created']

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        db_table = 'comment'


# класс movie для хранения фильмов в базе данных
class Movie(models.Model):
    # добавление n-количества жанров
    genre = models.ManyToManyField(
        'Genre',
        verbose_name='Жанр',
        help_text='Жанр'
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
    # год выхода фильма
    year = models.PositiveSmallIntegerField(
        default=2020,
        verbose_name='Год выхода',
        help_text='Год выхода',
    )
    # рейтинг фильма
    rating = models.FloatField(
        verbose_name='Рейтинг',
        help_text='Рейтинг',
    )
    # средняя оценка фильма
    avg_rating = models.FloatField(
        default=0,
        verbose_name='Средний рейтинг',
        help_text='Средний рейтинг',
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
    time = models.CharField(
        max_length=250,
        verbose_name='Время',
        help_text='Время',
    )
    # добавление n-количества актеров
    actors = models.ManyToManyField(
        'Actor',
        verbose_name='Актеры',
        help_text='Актеры',
    )
    # добавление n-количества режиссеров
    directors = models.ManyToManyField(
        'Director',
        verbose_name='Режиссеры',
        help_text='Режиссеры',
    )
    # добавление n-количества стран
    country = models.ManyToManyField(
        'Country',
        verbose_name='Страна',
        help_text='Страна',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['-release_date']
