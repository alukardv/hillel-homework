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
            "actor",
            "composer",
            "actress",
            "producer",
            "writer",
            "cinematographer",
        ]

    director = serializers.SerializerMethodField()
    actor = serializers.SerializerMethodField()
    composer = serializers.SerializerMethodField()
    actress = serializers.SerializerMethodField()
    producer = serializers.SerializerMethodField()
    writer = serializers.SerializerMethodField()
    cinematographer = serializers.SerializerMethodField()


    def get_director(self, object):
        director = PersonMovie.objects.filter(
            movie=object, job__startswith="director"
        ).first()
        if not director:
            return None
        return director.person.name

    def get_actor(self, object):
        actor = PersonMovie.objects.filter(
            movie=object, job__startswith="actor"
        ).first()
        if not actor:
            return None
        return actor.person.name

    def get_composer(self, object):
        composer = PersonMovie.objects.filter(
            movie=object, job__startswith="composer"
        ).first()
        if not composer:
            return None
        return composer.person.name

    def get_actress(self, object):
        actress = PersonMovie.objects.filter(
            movie=object, job__startswith="actress"
        ).first()
        if not actress:
            return None
        return actress.person.name

    def get_producer(self, object):
        producer = PersonMovie.objects.filter(
            movie=object, job__startswith="producer"
        ).first()
        if not producer:
            return None
        return producer.person.name

    def get_writer(self, object):
        writer = PersonMovie.objects.filter(
            movie=object, job__startswith="writer"
        ).first()
        if not writer:
            return None
        return writer.person.name

    def get_cinematographer(self, object):
        cinematographer = PersonMovie.objects.filter(
            movie=object, job__startswith="cinematographer"
        ).first()
        if not cinematographer:
            return None
        return cinematographer.person.name


class MovieDetailSerializer(MovieSerilalizer):
    class Meta:
        model = Movie
        fields = ["id", "name", "genres", "date", "director", "actor", "composer", "actress", "producer", "writer", "cinematographer",]

    persons = PersonSerializer(many=True)


