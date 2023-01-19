from django.core.management.base import BaseCommand
from django.utils.text import slugify
from movie.models import Genre

class Command(BaseCommand):
    help = "Создание жанров"

    def handle(self, *args, **options):
        genres = [
            "Боевик",
            "Вестерн",
            "Военный",
            "Детектив",
            "Драма",
            "Исторический",
            "Комедия",
            "Криминал",
            "Мелодрама",
            "Мультфильм",
            "Приключения",
            "Семейный",
            "Спорт",
            "Триллер",
            "Ужасы",
            "Фантастика"
        ]
        for genre in genres:
             Genre.objects.create(name=genre)
        self.stdout.write(self.style.SUCCESS("Жанры созданы"))
