from django.urls import path
from api.views import MovieAPI, AccountAPIView, GenreAPIView, CountryAPIView

urlpatterns = [
    path('movies/', MovieAPI.as_view(), name='movies'),  # ListAPIView - выводит список объектов.
    path('users/', AccountAPIView.as_view(), name='users'),  # ListAPIView - выводит список объектов. )
    path("genres/", GenreAPIView.as_view(), name="genres"),
    path("country/", CountryAPIView.as_view(),  name="countries"),
    path("country/<int:pk>/", CountryAPIView.as_view(), name="countries_update"),
]
