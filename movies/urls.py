from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from movies.views import Movies, MovieDetail, MovieCreate, MovieUpdate, MovieDelete

urlpatterns = [
    path('', cache_page(60)(Movies.as_view()), name='home'),
    path('movie/<slug:slug>', cache_page(60)(MovieDetail.as_view()), name='movie'),
    path('create', MovieCreate.as_view(), name='movie_create'),
    path('movie/<slug:slug>/update', MovieUpdate.as_view(), name='movie_update'),
    path('movie/<slug:slug>/delete', MovieDelete.as_view(), name='movie_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
