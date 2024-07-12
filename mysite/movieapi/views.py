from django.shortcuts import render
from myapp.models import Movie
from rest_framework import generics

from .serializers import MovieSerializer


class MovieAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
