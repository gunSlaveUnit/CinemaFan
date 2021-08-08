import uuid

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    slug = models.SlugField(max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    tagline = models.CharField(max_length=100, default='')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    poster = models.ImageField(upload_to="movies/")
    year = models.PositiveSmallIntegerField(default=2021)
    country = models.CharField(max_length=30)
    budget = models.PositiveIntegerField(default=0, help_text="$")
    fees_in_usa = models.PositiveIntegerField(default=0, help_text="$")
    fess_in_world = models.PositiveIntegerField(default=0, help_text="$")
    slug = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie', kwargs={'slug': self.slug})
