from django import forms
from movie.models import Movie, Episode


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'


