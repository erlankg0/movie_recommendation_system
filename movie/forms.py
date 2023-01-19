from django import forms
from movie.models import Movie, Episode


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'


class ExcludeEpisodeWidget(forms.SelectMultiple):
    def __init__(self, *args, **kwargs):
        super(ExcludeEpisodeWidget, self).__init__(*args, **kwargs)
        self.attrs.update({'size': '10'})

    def render_options(self, choices, selected_choices):
        # исключить эпизоды, которые уже добавлены в другой фильм
        used_episodes = Episode.objects.filter(movie__isnull=False).values_list('pk', flat=True)
        choices = [(pk, name) for pk, name in choices if pk not in used_episodes]
        return super().render_options(choices, selected_choices)