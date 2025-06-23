from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .forms import ReviewForm
from .models import Movie, Review, Genre

def movie_list(request):
    movies = Movie.objects.all()
    return render(request,
                  'site/movie/movie_list.html',
                  {'movies': movies})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    reviews = Review.objects.filter(movie=movie)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        reviews = Review.objects.filter(movie=movie)
        if form.is_valid():
            Review.objects.create(text = form.cleaned_data['text'],
                                  rating = form.cleaned_data['rating'],
                                  author = form.cleaned_data['author'],
                                  movie = movie)
            user_raiting = sum(Review.objects.filter(movie=movie).values_list('rating', flat=True))
            movie.rating = user_raiting / len(reviews)
            movie.save()
    else:
        form = ReviewForm()
    return render(request,
                  'site/movie/movie_detail.html',
                  {'movie': movie,
                   'reviews': reviews,
                   'form': form})

