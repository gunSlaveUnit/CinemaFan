from django.contrib import admin

from movies.models import Movie, Category, Position, Person, Genre, MovieScene, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('full_name',)}


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_filter = ('category', 'genres', 'year', 'country', 'budget')
    search_fields = ('title', 'tagline', 'description')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(MovieScene)
class MovieSceneAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('parent_review', 'email', 'username', 'text', 'movie')
    readonly_fields = ('email', 'username')
