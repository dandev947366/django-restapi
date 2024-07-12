from django.shortcuts import render
from myapp.models import Movie
from rest_framework import generics


class MovieAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
