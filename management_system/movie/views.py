from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
from .models import Movie
from .serializers import MovieListSerializer, MovieDetailSerializer


@api_view(['GET'])
def get_movies(request):
    movies = Movie.objects.all()

    serializer = MovieListSerializer(movies, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_frontpage_movies(request):
    movies = Movie.objects.all() [0:4]

    serializer = MovieListSerializer(movies, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def get_movie(request, slug):
    movie = Movie.objects.get(slug=slug)

    serializer = MovieDetailSerializer(movie)

    return Response(serializer.data)
