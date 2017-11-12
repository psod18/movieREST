from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from movies.serializers import MovieSerializer
from .models import (
    Person,
    Movie,
)


class MoviesView(APIView):

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True, context={"request": request})
        return Response(serializer.data)
