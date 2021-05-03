from .models import Artist, Album, Track
from django.shortcuts import get_object_or_404
from .serializers import ArtistSerializer, AlbumSerializer, TrackSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class ArtistViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing artist instances.
    """
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()


class AlbumViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing album instances.
    """
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()

class TrackViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing track instances.
    """
    serializer_class = TrackSerializer
    queryset = Track.objects.all()