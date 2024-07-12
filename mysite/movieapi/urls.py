from django.urls import path

from .views import MovieAPIView

urlpatterns = [path("movieapi/", MovieAPIView.as_view())]
