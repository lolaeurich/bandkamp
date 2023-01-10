from rest_framework import serializers

from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(max_length=255)
    # year = serializers.IntegerField()
    # user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Album
        fields = '__all__'
        read_only_fields = ['id, user_id']

    def create(self, validated_data):
        return Album.objects.create(**validated_data)
