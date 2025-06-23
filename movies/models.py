from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, default='')
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    year = models.IntegerField()
    description = models.TextField(blank=True)
    rating = models.DecimalField(max_digits=3,
                                 decimal_places=1,
                                 default='')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(Movie,
                             related_name='reviews',
                             on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField()

    author = models.CharField(max_length=50)

    publish = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


