import json

from django.views import View
from django.http import JsonResponse
from .models import Movie, Actor

class MovieListView(View):
    def get(self, request):
        movies = Movie.objects.all()
        result = []
        
        for movie in movies :
            actors = movie.m2m.all()
            actor_list=[]
            for actor in actors:
                name = actor.first_name+actor.last_name
                actor_list.append(name)
            
            text = {'title':movie.title, 'release_date':movie.release_data, 'running_time':movie.running_time, 'actor':actor_list}
            result.append(text)

        return JsonResponse({'result':result},status=200)
        
class ActorListView(View):
    def get(self, request):
        actors = Actor.objects.all()
        result = []

        for actor in actors:
            movies = actor.movie_actor.all()
            movie_list = []
            for movie in movies:
                movie_list.append(movie.title)

            text = {'first_name':actor.first_name,'last_name':actor.last_name,'date_of_birth':actor.data_of_birth,'movie':movie_list}
            result.append(text)
                        
        return JsonResponse({'result':result},status=200)
