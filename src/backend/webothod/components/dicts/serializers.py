from rest_framework import serializers

from .models import Regions, QueryType
from ..companies.models import CompanyRegion


class RegionsSerializer(serializers.ModelSerializer):
    value = serializers.SerializerMethodField(help_text='Идентификатор для select')

    class Meta:
        model = Regions
        fields = ('code', 'value', 'text')

    def get_value(self, el):
        return el.code


class CompanyRegionsSerializer(serializers.ModelSerializer):
    code = serializers.SerializerMethodField()
    text = serializers.SerializerMethodField()

    class Meta:
        model = CompanyRegion
        fields = ('code', 'text')

    @staticmethod
    def get_code(el):
        return el.first().region.code

    @staticmethod
    def get_text(el):
        return el.first().region.text


class QueryTypesSerializer(serializers.ModelSerializer):
    value = serializers.SerializerMethodField(help_text='Идентификатор для select')

    class Meta:
        model = QueryType
        fields = ('value', 'text')

    def get_value(self, el):
        return el.id
