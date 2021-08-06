from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from movies.views import Movies, Movie

urlpatterns = [
    path('', Movies.as_view(), name='home'),
    path('movie/<slug:slug>', Movie.as_view(), name='movie'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
