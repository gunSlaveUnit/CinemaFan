from django.views.generic import ListView

from movies.models import Movie


class Movies(ListView):
    queryset = Movie.objects.all()
