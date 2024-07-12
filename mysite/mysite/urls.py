from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from myapp.views import MovieAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("movieapi/", include("movieapi.urls")),
    path("movies/", MovieAPIView.as_view(), name="movie-list"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
