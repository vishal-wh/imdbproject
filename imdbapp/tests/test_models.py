import datetime
from django.test import TestCase
from imdbapp.models import (
   Movie, Genre
)

class MovieTest(TestCase):
    def setUp(self):
        self.create_date = datetime.datetime.now()
        self.edit_date = datetime.datetime.now()
        self.genre = Genre.objects.create(name = 'AB')

    def test_movie_save_minimum_fields(self):
        movie = Movie.objects.create(name='ABCD')
        saved_obj = Movie.objects.get(pk=movie.pk)
        assert saved_obj.name == 'ABCD'

    def test_movie_save_all_fields(self):

        movie = Movie.objects.create(
            name='ABCD',
            director='ABCD',
            imdb_score= 7.8,
            popularity=90.05,
            create_date=self.create_date,
            edit_date=self.edit_date,
        )
        movie.genre.add(self.genre)
        saved_obj = Movie.objects.get(pk=movie.pk)
        assert saved_obj.name == 'ABCD'

    def test_movie_save_empty_fields(self):
        movie = Movie.objects.create()
        saved_obj = Movie.objects.get(pk=movie.pk)
        self.assertTrue(saved_obj, True)
