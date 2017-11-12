from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=256)


class Movie(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    director = models.ForeignKey(Person, related_name='%(class)s_director')
    actors = models.ManyToManyField(Person, through='Role', related_name='%(class)s_actors')
    year = models.IntegerField()


class Role(models.Model):
    person = models.ForeignKey(Person)
    movie = models.ForeignKey(Movie)
    role = models.CharField(max_length=256)
