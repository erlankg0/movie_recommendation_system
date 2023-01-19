from movie.models import Genre


def get_all_genres(request):
    return  dict(genres=Genre.objects.all())
