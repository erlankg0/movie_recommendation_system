from rest_framework import serializers

from accounts.models import Account
from movie.models import Movie, Genre, Country


class MovieSerializer(serializers.ModelSerializer):
    class Meta:  # Мета данные.
        model = Movie  # Модель.
        fields = '__all__'  # Все поля.


class AccountSerializer(serializers.ModelSerializer):
    class Meta:  # Мета данные.
        model = Account  # Модель.
        fields = '__all__'  # Все поля.


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["name", "slug"]


# -------------------------Manual---------------------------

class CountrySerializer(serializers.Serializer):
    name = serializers.CharField(
        max_length=100,
    )
    slug = serializers.SlugField(
        max_length=100,
    )

    def create(self, validated_data):
        return Country.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.slug = validated_data.get("slug", instance.slug)
        instance.save()
        return instance
