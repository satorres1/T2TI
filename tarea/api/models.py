from django.db import models

class Artist(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Album(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)


class Track(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    duration = models.FloatField()
    times_played = models.IntegerField()