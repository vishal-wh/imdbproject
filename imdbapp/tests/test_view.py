import json
from imdbapp.models import Movie
from imdbapp.serializer import MovieSerializer
import datetime
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory

# initialize client
client = Client()

class GetAllMovieTest(TestCase):
    """ Test module for GET all movie """
    def setUp(self):
        self.movie = Movie.objects.create(name='ABCD')
        self.factory = APIRequestFactory()
        self.request = self.factory.get('/')
        self.serializer_context = {'request': Request(self.request)}

    def test_list_all_movie(self):
        # get API response
        response = client.get('/movie/')
        # get data from db
        movie = Movie.objects.filter(name='ABCD')
        serializer = MovieSerializer(
            movie, many=True, context=self.serializer_context
        )
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleMovieTest(TestCase):
    """ Test module for GET single movie """
    def setUp(self):
        self.movie = Movie.objects.create(name='ABCD')
        self.factory = APIRequestFactory()
        self.request = self.factory.get('/')
        self.serializer_context = {'request': Request(self.request)}

    def test_get_valid_single_movie(self):
        # Test get valid single movie
        url = reverse('movie-detail', kwargs={'pk': self.movie.pk})
        response = client.get(url)
        movie = Movie.objects.get(pk=self.movie.pk)
        serializer = MovieSerializer(movie, context=self.serializer_context)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_movie(self):
        # Test to check if get single movie for invalid id
        url = reverse('movie-detail', kwargs={'pk': 4330})
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewMovieTest(TestCase):
    """ Test module for inserting a new movie """
    def setUp(self):
        self.create_date = '2021-06-19T10:37:10.480391+00:00',
        self.edit_date = '2021-06-19T10:37:10.480391+00:00',
        self.valid_payload = {
                'name': 'ABCD',
                'director': 'ABCD',
                'imdb_score': 9,
                'popularity': 80,
                "create_date":self.create_date,
                "edit_date": self.edit_date
        }
        self.invalid_payload = {
            "name": "ABCD",
            "director": "ABCD",
            "imdb_score": 90,
            "popularity": 190,
            "create_date": self.create_date,
            "edit_date": self.edit_date
        }

    def test_create_valid_movie(self):
        response = client.post(
            reverse('movie-list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_movie(self):
        response = client.post(
            reverse('movie-list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleMovieTest(TestCase):
    """Test module for updating an existing movie """
    def setUp(self):
        self.create_date ='2021-06-19T10:37:10.480391+00:00'
        self.edit_date = '2021-06-19T10:37:10.480391+00:00'
        self.valid_payload = {
            "name": "ABCD",
            "director": "ABCD",
            "imdb_score": 9.0,
            "popularity": 90,
            "create_date": self.create_date,
            "edit_date": self.edit_date
        }

    def test_valid_update_movie(self):
        # create movie to update
        response = client.post(
            reverse('movie-list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json',
        )
        update_payload = {
            'id': response.data['id'],
            "name": "ABCD",
            "director": "ABCD",
            "imdb_score": 9.0,
            "popularity": 19.0,
            "create_date": self.create_date,
            "edit_date": self.edit_date

        }
        # Update movie
        response = client.put(
            reverse('movie-detail', kwargs={'pk': response.data['id']}),
            data=json.dumps(update_payload),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_movie(self):
        response = client.post(
            reverse('movie-list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json',
        )
        invalid_updated_data = {
            'id': response.data['id'],
            "name": "ABCD",
            "director": "ABCD",
            "imdb_score": 90,
            "popularity": 190,
            "create_date": self.create_date,
            "edit_date": self.edit_date
        }
        put_response = client.put(
            reverse('movie-detail', kwargs={'pk': response.data['id']}),
            data=json.dumps(invalid_updated_data),
            content_type='application/json',
        )
        self.assertEqual(put_response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteMovieTest(TestCase):
    """ Test module for deleting an existing movie """
    def setUp(self):
        self.movie = Movie.objects.create(name='ABCD')

    def test_valid_delete_movie(self):
        response = client.delete(
            reverse('movie-detail', kwargs={'pk': self.movie.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_movie(self):
        response = client.delete(
            reverse('movie-detail', kwargs={'pk': 300}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
