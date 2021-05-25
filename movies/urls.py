from django.urls import path,include
from .views import MovieListView, ActorListView


urlpatterns = [
    path('movie', MovieListView.as_view()),
    path('actor', ActorListView.as_view())
]