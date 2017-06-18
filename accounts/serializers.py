from rest_framework import serializers

from accounts.models import Account
from aroma.models import Aroma


class MyFavoritesSerializer(serializers.ModelSerializer):
    favorites = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Account
        fields = ('id', 'favorites')


class MyCollectionSerializer(serializers.ModelSerializer):
    collection = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Account
        fields = ('id', 'collection')