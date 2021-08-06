from django.views.generic import ListView, DetailView, CreateView

from movies.models import Movie


class Movies(ListView):
    model = Movie
    queryset = Movie.objects.all()
    context_object_name = 'movies'


class Movie(DetailView):
    model = Movie
    slug_field = 'slug'
    context_object_name = 'movie'


class CreateMovie(CreateView):
    model = Movie
