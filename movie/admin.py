from django.contrib import admin
from django.template.loader import render_to_string

from movie.models import Movie, Genre, Comment, Country, Actor, Director, Tag, Episode
from movie.forms import MovieForm, ExcludeEpisodeWidget
from django.db import models


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    form = MovieForm

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # get current movie name
        form.base_fields['episodes'].queryset = form.base_fields['episodes'].queryset.exclude(used=True)
        return form

    # при добавлении эпизода в фильм, пометить его как использованный
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        obj.episodes.update(used=True)  # обновить статус эпизода на использованный
        obj.save()

    def episodes_list(self, obj):
        return render_to_string('movie/episodes_list.html', {'episodes': obj.episodes.all()})

    # отображение эпизодов в админке
    episodes_list.short_description = 'Эпизоды'

    list_display = ('title', "episodes_list")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')
    list_display_links = ('name', 'slug')
    search_fields = ('name', 'slug')


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    pass


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')
    list_display_links = ('name', 'slug')
    list_filter = ('name', 'slug')
    search_fields = ('name', 'slug')


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    pass
# Register your models here.
