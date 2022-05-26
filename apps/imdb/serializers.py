from collections import OrderedDict

from django.db.models import Avg
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from apps.imdb.models import Movie, Person, PersonMovie


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ["id", "name", "rating_avg"]

    rating_avg = serializers.SerializerMethodField()

    def get_rating_avg(self, object):
        person_movie = PersonMovie.objects.filter(person=object).all()
        rating_avg = 0.0
        count = 0
        for i in person_movie:
            if i.movie.rating > 0.0:
                count += 1
                rating_avg += i.movie.rating
        return rating_avg / count


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
            "rating",
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
            "rating",
        ]

    participants = serializers.SerializerMethodField()

    def get_participants(self, movie_obj):
        participants = PersonMovie.objects.filter(movie=movie_obj).all()
        if participants.count() > 0:
            tmp = []
            for p in participants:
                tmp.append(
                    {
                        'p_imdb_id': p.person.pk,
                        'name': p.person.name,
                        'position': p.category,
                        'role': p.characters,
                    }
                )
            return tmp
        return '*no_participants*'

    #rating_actor = serializers.SerializerMethodField()
    #
    # def get_rating_actor(self, object):
    #     rating_actor = Person.objects.get() Movie.objects.filter(movies=2006).aggregate(Avg('rating'))
    #     if not rating_actor:
    #         return None
    #     return rating_actor


