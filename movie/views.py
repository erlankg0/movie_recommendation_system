from django.shortcuts import render
from movie.models import Movie


# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {"movies": movies}
    return render(request, 'movie/index.html', context)

def detail(request, pk):
    movie = Movie.objects.get(id=pk)
    context = {"movie": movie}
    return render(request, 'movie/detail.html', context)