from django.core.management.base import BaseCommand
from movie.models import Movie, Genre, Comment, Country, Actor, Director
from account.models import Gender


class Command(BaseCommand):
    help = 'Заполнение таблиц БД данными'

    def handle(self, *args, **options):
        if not Movie.objects.count():
            genre = Genre.objects.create(
                name='драма'
            )
            actor = Actor.objects.create(
                name='Джонни Депп',
                gender=Gender.objects.get(id=1),
                age=55,
                description='Американский актер и продюсер',
                image='actors/actor.jpg',
                slug='johnny-depp'
            )
            director = Director.objects.create(
                name='Мартин Скорсезе',
                gender=Gender.objects.get(id=2),
                age=76,
                description='Американский режиссер',
                image='directors/director.jpg',
                slug='martin-scorsese'
            )
            country = Country.objects.create(
                name='США'
            )
            movie = Movie.objects.create(
                title='Джокер',
                tagline='Все начинается с смеха',
                description='Фильм расскажет о том, как из маленького человека с низким статусом в обществе стал самый опасный преступник в Нью-Йорке.',
                poster='movies/movie.jpg',
                year=2019,
                slug='joker'
            )

            genre = Genre.objects.create(
                name='комедия'
            )
            movie.genre.add(genre)
            movie.actors.add(actor)
            movie.director.add(director)
            movie.save()
