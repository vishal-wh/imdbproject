from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializer import *
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .permissions import UserPermission
import django_filters.rest_framework
from rest_framework import filters

class  MovieViewSet(ModelViewSet):
    """
       list:
           Return a list of all the existing Lenders.
       create:
           Create a new Lenders.
       retrieve:
           Return the given Lenders.
       update:
           Update the given Lenders.
       destroy:
           Delete the given Lenders.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (UserPermission,) # Permission for superuser and read only permission for authenticate user
    filter_backends = (
        django_filters.rest_framework.DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    )
    search_fields = (
        'name',
        'director',
        'imdb_score',
        'popularity',
        'genre__name',  # search movies by genre name as genre is many to many relationship with movies
    )
    ordering_fields = (
        'name',
        'imdb_score',
        'popularity',
        'director',
    )
    filter_fields = {
        'name': ['exact', 'iexact'],
        'genre__name': ['exact', 'iexact']
    }

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(MovieViewSet, self).dispatch(*args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer =  MovieSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer =  MovieSerializer(queryset, many=True)
        return Response(serializer.data)
