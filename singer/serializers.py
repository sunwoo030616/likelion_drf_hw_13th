from rest_framework import serializers
from .models import *

class SingerSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    created_at = serializers.CharField(read_only=True)
    updated_at = serializers.CharField(read_only=True)

    songs = serializers.SerializerMethodField(read_only=True)

    def get_songs(self, instance):
        serializer = SongSerializer(instance.songs, many=True)
        return serializer.data 
    class Meta:
        model = Singer
        fields = ['id', 'name', 'content', 'debut', 'created_at', 'updated_at', 'songs']


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
        read_only_fields = ['singer']