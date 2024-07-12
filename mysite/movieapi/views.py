from django.shortcuts import render
from myapp.models import Movie
from rest_framework import generics

from .serializers import MovieSerializer


class MovieAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
