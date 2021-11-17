from rest_framework import serializers

from .models import Regions, QueryType


class RegionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regions
        fields = ('code', 'text')


class QueryTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = QueryType
        fields = ('id', 'text')
