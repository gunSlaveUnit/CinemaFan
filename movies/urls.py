from django.urls import path

from movies.views import Movies

urlpatterns = [
    path('', Movies.as_view(), name='home'),
]
