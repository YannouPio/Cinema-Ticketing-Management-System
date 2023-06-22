from rest_framework import serializers

from .models import Movie

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'slug', 'short_description', 'get_image')


class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'slug', 'short_description', 'long_description')
