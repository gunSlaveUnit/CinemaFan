# TODO: add movie scenes and reviews
# TODO: add 3**, 4** and 5** handlers
# TODO: add tags
# TODO: tickets

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from movies.forms import ReviewForm
from movies.models import Movie


class Movies(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    context_object_name = 'movies'
    paginate_by = 5
    ordering = ('title',)
    extra_context = {'title': 'Welcome to the club, buddy'}


class MovieDetail(DetailView):
    model = Movie
    slug_field = 'slug'
    context_object_name = 'movie'
    extra_context = {'title': 'movie.title'}


class MovieCreate(LoginRequiredMixin, CreateView):
    model = Movie
    fields = '__all__'
    template_name = 'movies/movie_create.html'
    extra_context = {'title': "So, you want to create a new movie for our service"}

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class MovieUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Movie
    fields = '__all__'
    template_name = 'movies/movie_create.html'
    extra_context = {'title': "Oh, something is wrong?"}

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
    extra_context = {'title': "You want to delete something. Ok"}

    def test_func(self):
        movie = self.get_object()
        if self.request.user == movie.author:
            return True
        return False


class AddReview(View):
    def post(self, request, slug):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(slug=slug)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())
