from .models import (
    Movie,
    Person,
    Role,
)
from rest_framework import serializers


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('name', )


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    director = PersonSerializer(read_only=False)
    actors = PersonSerializer(read_only=False, many=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'director', 'actors', 'year']


class RoleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Role
        fields = '__all__'

