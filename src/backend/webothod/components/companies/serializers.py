from rest_framework import serializers
import json

from .models import Companies, CompanyWasteCodes
from ..dicts.serializers import RegionsSerializer
from ..waste_codes.serializers import WasteCodesSerializer


class CompaniesSerializer(serializers.ModelSerializer):
    gps = serializers.SerializerMethodField(help_text='GPS')
    phones = serializers.SerializerMethodField(help_text='Телефоны')
    emails = serializers.SerializerMethodField(help_text='Emails')
    activity = serializers.SerializerMethodField(help_text='Типы отходов с которыми работает')
    site = serializers.SerializerMethodField(help_text='Сайт')
    region = RegionsSerializer(help_text='Регион')

    class Meta:
        model = Companies
        fields = (
            'itn',
            'locality',
            'phones',
            'emails',
            'site',
            'name',
            'gps',
            'region',
            'activity',
        )

    @staticmethod
    def get_gps(el):
        if el.gps is not None:
            return json.loads(el.gps)
        else:
            return None

    @staticmethod
    def get_phones(el):
        if el.phones:
            return json.loads(el.phones)
        else:
            return None

    @staticmethod
    def get_emails(el):
        if el.emails:
            return json.loads(el.emails)
        else:
            return None

    @staticmethod
    def get_site(el):
        if el.site:
            try:
                data = json.loads(el.site)
            except:
                try:
                    data = json.loads("[\"{}\"]".format(el.site))
                except:
                    data = None
            print(el.site)
            return data
        else:
            return None

    @staticmethod
    def get_activity(el):
        if el.activity:
            return json.loads(el.activity)
        else:
            return None


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
