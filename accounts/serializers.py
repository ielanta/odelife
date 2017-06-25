from rest_framework import serializers

from accounts.models import Account


class UserSerializer(serializers.ModelSerializer):
    profile_url = serializers.SerializerMethodField()
    class Meta:
        model = Account
        fields = ('id', 'get_full_name', 'profile_url')


    @staticmethod
    def get_profile_url(obj):
        return obj.account.get_absolute_url()