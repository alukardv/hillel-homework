from rest_framework import permissions
from rest_framework.generics import (
    ListCreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)

from apps.imdb.models import Movie
from apps.imdb.serializers import MovieSerilalizer, MovieDetailSerializer


class MyView(ListCreateAPIView):
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = MovieSerilalizer
    queryset = Movie.objects.all().prefetch_related("persons")


class MovieRetrieveUpdateView(RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerilalizer
    queryset = Movie.objects.all().prefetch_related("persons")

class MovieDetailRetrieveUpdateView(RetrieveUpdateDestroyAPIView):
    serializer_class = MovieDetailSerializer
    queryset = Movie.objects.all().prefetch_related("persons")
