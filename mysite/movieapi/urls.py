from django.urls import path

from .views import MovieAPIView, MovieDetail

urlpatterns = [
    path("", MovieAPIView.as_view(), name="movie-list"),
    path("<int:pk>/", MovieDetail.as_view(), name="movie-detail"),
]
