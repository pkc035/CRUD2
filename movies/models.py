from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=45)
    release_data = models.DateField()
    running_time = models.IntegerField()
    m2m = models.ManyToManyField('Actor',related_name='movie_actor')

    class Meta :
        db_table = 'movies'


class Actor(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    data_of_birth = models.DateField()

    class Meta :
        db_table = 'actors'


# class Actor_movie(models.Model):
#     actor_id = models.ForeignKey(Actor,on_delete=models.CASCADE)
#     movie_id = models.ForeignKey(Movie,on_delete=models.CASCADE)

#     class Meta :
#         db_table = 'actors_movies'