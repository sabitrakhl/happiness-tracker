from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from info.models import HappinessInfo


class InfoCreateSerializer(ModelSerializer):
    class Meta:
        model = HappinessInfo
        fields = [
            'happiness_level',
        ]


class InfoRetrieveSerializer(Serializer):
    level = serializers.IntegerField(source='happiness_level')
    count = serializers.IntegerField()


