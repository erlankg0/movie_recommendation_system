from django.urls import path
from movie.views import index, detail

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', detail, name='detail'),
]
