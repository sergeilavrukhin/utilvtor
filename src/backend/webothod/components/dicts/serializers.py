from rest_framework import serializers

from .models import Regions, QueryType


class RegionsSerializer(serializers.ModelSerializer):
    value = serializers.SerializerMethodField(help_text='Идентификатор для select')

    class Meta:
        model = Regions
        fields = ('code', 'value', 'text')

    def get_value(self, el):
        return el.code


class QueryTypesSerializer(serializers.ModelSerializer):
    value = serializers.SerializerMethodField(help_text='Идентификатор для select')

    class Meta:
        model = QueryType
        fields = ('value', 'text')

    def get_value(self, el):
        return el.id
