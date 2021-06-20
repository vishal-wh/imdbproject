from rest_framework import serializers
from imdbapp.models import *

class GenreSerializer(serializers.ModelSerializer):
    """
      Serializer for genre model
      """
    class Meta:
        model = Genre
        fields = ('name',)

class MovieSerializer(serializers.ModelSerializer):
    """
      Serializer for movie model
    """
    genre = GenreSerializer(many=True, read_only=True)  # To get response in nested form, use nested serializer
    genre = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = (
                  'id',
                  'name',
                  'director',
                  'genre',
                  'imdb_score',
                  'popularity',)

    def get_genre(self, obj):
        """
        To get genre model response in list format, rather than dictionary key value format, as Django by default provides
        "genre": ["Adventure"," Family"," Fantasy"," Musical"],
        """
        return [sub['name'] for sub in obj.genre.values() if sub['name'] is not None]


