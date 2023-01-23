from django.forms import model_to_dict  #
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Account
from api.serializers import MovieSerializer, AccountSerializer, GenreSerializer, CountrySerializer
from movie.models import Movie, Genre, Country
from datetime import datetime


class MovieAPI(APIView):
    def get(self, request):  # Выводит список объектов.
        movies = Movie.objects.all()  # Получаем все объекты.
        serializer = MovieSerializer(movies,
                                     many=True)  # Сериализуем. many=True - указывает что у нас не один объект, а много.
        return Response({"movies": serializer.data})

    def post(self, request):
        movie = Movie.objects.create(
            title=request.data["title"],
            description=request.data['description'],
            slogan=request.data["slogan"],
            release_date=datetime.strptime(request.data["release_date"], "%Y-%d-%m"),
            year=request.data["year"],
            rating=request.data["rating"],
            avg_rating=request.data["avg_rating"],
            poster=request.data["poster"],
            video=request.data["video"],
            time=request.data["time"],
            budget=request.data["budget"],
        )
        print(request.data)
        return Response({"message": model_to_dict(movie)})


class AccountAPIView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class GenreAPIView(APIView):
    def get(self, request):
        genres = Genre.objects.all()
        serializers = GenreSerializer(
            genres,
            many=True
        )
        return Response({"genres": serializers.data})

    def post(self, request):
        genre = Genre.objects.create(
            name=request.data["name"],
        )
        return Response({"genre": model_to_dict(genre)})


class CountryAPIView(APIView):
    def get(self, request):
        countries = Country.objects.all()
        return Response({"get": CountrySerializer(countries, many=True).data})

    def post(self, request):
        serializer = CountrySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # проверка на валидность данных
        serializer.save()
        return Response({"post": serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})
        else:
            try:
                instance = Country.objects.get(pk=pk)
                print(instance)
            except KeyError:
                return Response({"error": "Object does not exists"})
            serializer = CountrySerializer(data=request.data, instance=instance)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"put": serializer.data})
