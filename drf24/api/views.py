from django.shortcuts import render
from rest_framework import viewsets
from .models import Song, Singer
from .serializers import SongSerializer, SingerSerializer

# Create your views here.
class SingerAPI(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

class SongAPI(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer    