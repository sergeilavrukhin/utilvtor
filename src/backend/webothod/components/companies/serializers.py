from rest_framework import serializers
import json

from .models import Companies, CompanyWasteCodes
from ..dicts.serializers import CompanyRegionsSerializer
from ..waste_codes.serializers import WasteCodesSerializer


class CompaniesSerializer(serializers.ModelSerializer):
    latitude = serializers.FloatField(help_text='Широта')
    longitude = serializers.FloatField(help_text='Долгота')

    phones = serializers.StringRelatedField(source='company_phones', help_text='Телефоны',
                                            read_only=True, many=True)
    emails = serializers.StringRelatedField(source='company_emails', help_text='Emails',
                                            read_only=True, many=True)
    activity = serializers.SerializerMethodField(help_text='Типы отходов с которыми работает')
    sites = serializers.StringRelatedField(source='company_sites', help_text='Сайты',
                                           read_only=True, many=True)
    regions = CompanyRegionsSerializer(
        source='company_region_company',
        help_text='Регионы',
        read_only=True,
        many=True,
    )

    region = CompanyRegionsSerializer(
        source='company_region_company',
        help_text='Регион',
        read_only=True,
        many=False,
    )

    actual_at = serializers.SerializerMethodField(help_text='Дата и время создания')

    class Meta:
        model = Companies
        fields = (
            'itn',
            'locality',
            'phones',
            'emails',
            'sites',
            'name',
            'latitude',
            'longitude',
            'region',
            'regions',
            'activity',
            'actual',
            'actual_at',
        )

    @staticmethod
    def get_activity(el):
        if el.activity:
            return json.loads(el.activity)
        else:
            return None

    @staticmethod
    def get_actual_at(el):
        return el.actual_at.timestamp()


class CompanyWasteCodesSerializer(serializers.ModelSerializer):
    activity = serializers.SerializerMethodField(help_text='Типы отходов с которыми работает')
    waste_code = WasteCodesSerializer(help_text='Отход')

    class Meta:
        model = CompanyWasteCodes
        fields = ('activity', 'waste_code')

    @staticmethod
    def get_activity(el):
        if el.activity:
            return json.loads(el.activity)
        else:
            return None
