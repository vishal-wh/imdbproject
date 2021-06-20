import datetime
from django.test import TestCase
from imdbapp.models import Movie
from imdbapp.serializer import MovieSerializer


class MovieSerializerTest(TestCase):

    def setUp(self):
        self.movie = Movie.objects.create(name = 'ABCD',)
        self.serializer = MovieSerializer(instance=self.movie)

    def test_contains_expected_fields(self):
        """
        verifies if the serializer has the exact attributes it is expected
        to have
        """
        data = self.serializer.data
        self.assertEqual(
            set(data.keys()),
            set([
                 'id',
                 'name',
                 'director',
                 'imdb_score',
                 'popularity',
                 'genre',
                ]),)