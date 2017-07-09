from rest_framework import serializers

from accounts.models import Account


class UserSerializer(serializers.ModelSerializer):
    profile_url = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = Account
        fields = ('id', 'full_name', 'profile_url')

    @staticmethod
    def get_full_name(obj):
        return obj.account.get_full_name()

    @staticmethod
    def get_profile_url(obj):
        return obj.account.get_absolute_url()