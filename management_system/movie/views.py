from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
from .models import Movie, Category
from .serializers import MovieListSerializer, MovieDetailSerializer, CategoryListSerializer
from django.db.models import Q

@api_view(['GET'])
def search_movies(request):
    query = request.GET.get('query', '')
    movies = Movie.objects.filter(Q(title__icontains=query))
    serializer = MovieListSerializer(movies, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def get_categories(request):
    categories = Category.objects.all()

    serializer = CategoryListSerializer(categories, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def get_movies(request):

    category_id = request.GET.get('category_id', '')
    movies = Movie.objects.all()

    if category_id:
        movies = movies.filter(categories__id=int(category_id))


    serializer = MovieListSerializer(movies, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def get_frontpage_movies(request):
    movies = Movie.objects.all()[0:4]

    serializer = MovieListSerializer(movies, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def get_movie(request, slug):
    movie = Movie.objects.get(slug=slug)

    serializer = MovieDetailSerializer(movie)

    return Response(serializer.data)
