from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import movieSerializer
from .models import movie

# Create your views here.
class movieViewSet(viewsets.ModelViewSet):
    serializer_class = movieSerializer
    queryset = movie.objects.all()