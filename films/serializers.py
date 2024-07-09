from rest_framework import serializers
from .models import Movie

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'created_at']