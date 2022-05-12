from collections import OrderedDict

from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from apps.imdb.models import Movie, Person, PersonMovie


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ["id", "name"]


class MovieSerilalizer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            "id",
            "name",
            "genres",
            "date",
            "director",
            "persons",
        ]


    director = serializers.SerializerMethodField()



    def get_director(self, object):
        director = PersonMovie.objects.filter(
            movie=object, job__startswith="director"
        ).first()
        if not director:
            return None
        return director.person.name


class MovieDetailSerializer(MovieSerilalizer):
    class Meta:
        model = Movie
        fields = [
            "id",
            "name",
            "director",
            "date",
            "genres",
            "participants",
        ]

    participants = serializers.SerializerMethodField()

    def get_participants(self, movie_obj):
        participants = PersonMovie.objects.filter(movie=movie_obj).all()
        if participants.count() > 0:
            tmp = []
            for p in participants:
                tmp.append(
                    {
                        'p_imdb_id': p.person.imdb_id,
                        'name': p.person.name,
                        'position': p.category,
                        'role': p.characters,
                    }
                )
            return tmp
        return '*no_participants*'



