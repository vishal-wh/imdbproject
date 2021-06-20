from django.core.management.base import BaseCommand
from imdbapp.models import Movie, Genre
import json
import os

class Command(BaseCommand):
    # crete command to load movie data through json
    help = 'create movies data into movie model database'

    def handle(self, *args, **options):
        self.stdout.write('Run this command only once')
        file_path = os.path.dirname(os.path.realpath(
            __file__)) + '/imdb.json'

        with open(file_path) as json_file:
            data = json.load(json_file) # load movie json file
            # Get data and create movie in model database
            for info in data:
                list_genre = info.get('genre')
                movie_instance = Movie.objects.filter(name=info.get('name')).first()
                if not movie_instance:
                    movie_info= Movie.objects.create(
                    name=info.get('name'),
                    director = info.get('director'),
                    imdb_score = info.get('imdb_score'),
                    popularity = info.get('99popularity')
                    )
                    for genr in list_genre:
                        genre_type = Genre.objects.filter(name=genr).first()
                        if not genre_type:
                            genre_type = Genre(name=genr)
                            genre_type.save()
                        movie_info.genre.add(genre_type)
                        movie_info.genre.all()

