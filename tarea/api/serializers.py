from rest_framework import serializers
from .models import Artist, Album, Track
import pdb

class ArtistSerializer(serializers.ModelSerializer):
    self = serializers.SerializerMethodField('url')
    albums = serializers.SerializerMethodField('albunes')
    tracks = serializers.SerializerMethodField('canciones')
    
    class Meta:
        model = Artist
        fields = ['id', 'name', 'age', 'self', 'albums', 'tracks']


    def url(self, obj):
        path = self.context['request'].build_absolute_uri()
        final_path = path + str(obj.id)
        return final_path
    
    def albunes(self, obj):
        path = self.context['request'].build_absolute_uri()
        final_path = path + str(obj.id) + '/albums'
        return final_path
    
    def canciones(self, obj):
        path = self.context['request'].build_absolute_uri()
        final_path = path + str(obj.id) + '/tracks'
        return final_path

class AlbumSerializer(serializers.ModelSerializer):
    self = serializers.SerializerMethodField('url')
    artist = serializers.SerializerMethodField('artista')
    tracks = serializers.SerializerMethodField('canciones')
    class Meta:
        model = Album
        fields = ['id', 'artist_id', 'name', 'genre', 'self', 'artist', 'tracks']

    def url(self, obj):
        path = self.context['request'].build_absolute_uri()
        final_path = path + str(obj.id)
        return final_path
    
    def artista(self, obj):
        path = self.context['request'].build_absolute_uri()
        final_path = path + str(obj.id) + '/albums'
        return final_path
    
    def canciones(self, obj):
        path = self.context['request'].build_absolute_uri()
        final_path = path + str(obj.id) + '/tracks'
        return final_path

class TrackSerializer(serializers.ModelSerializer):
    self = serializers.SerializerMethodField('url')
    class Meta:
        model = Track
        fields = ['id', 'album_id', 'name', 'duration', 'times_played', 'self']

    def url(self, obj):
        path = self.context['request'].build_absolute_uri()
        final_path = path + str(obj.id)
        return final_path

