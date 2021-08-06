from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView

from movies.models import Movie


class Movies(ListView):
    model = Movie
    queryset = Movie.objects.all()
    context_object_name = 'movies'


class MovieDetail(DetailView):
    model = Movie
    slug_field = 'slug'
    context_object_name = 'movie'


class MovieCreate(LoginRequiredMixin, CreateView):
    model = Movie
    fields = '__all__'
    template_name = 'movies/movie_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
