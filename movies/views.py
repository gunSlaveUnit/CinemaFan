# TODO: add categories
# TODO: customize models in admin panel
# TODO: add 3**, 4** and 5** handlers
# TODO: add tags

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from movies.models import Movie


class Movies(ListView):
    model = Movie
    queryset = Movie.objects.filter({'draft': False})
    context_object_name = 'movies'
    paginate_by = 1
    ordering = ('title',)


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


class MovieUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Movie
    fields = '__all__'
    template_name = 'movies/movie_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        movie = self.get_object()
        if self.request.user == movie.author:
            return True
        return False


class MovieDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Movie
    fields = '__all__'
    context_object_name = 'movie'
    success_url = '/'

    def test_func(self):
        movie = self.get_object()
        if self.request.user == movie.author:
            return True
        return False
