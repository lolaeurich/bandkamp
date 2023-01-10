from rest_framework import serializers

from .models import Song


class SongSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(max_length=255)
    # duration = serializers.CharField(max_length=255)
    # album_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Song
        fields = '__all__'
        read_only_fields = ['id, album_id']

    def create(self, validated_data):
        return Song.objects.create(**validated_data)
