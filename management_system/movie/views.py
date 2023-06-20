from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
from .models import Movie
from .serializers import MovieListSerializer

@api_view(['GET'])
def get_movies(request):
    movie = Movie.objects.all()
    
    serializer = MovieListSerializer(movie, many = True)

    return Response(serializer.data)