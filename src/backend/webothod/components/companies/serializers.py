from rest_framework import serializers
import json

from .models import Companies
from ..dicts.serializers import RegionsSerializer


class CompaniesSerializer(serializers.ModelSerializer):
    gps = serializers.SerializerMethodField(help_text='GPS')
    phones = serializers.SerializerMethodField(help_text='Телефоны')
    emails = serializers.SerializerMethodField(help_text='Emails')
    region = RegionsSerializer(help_text='Регион')

    class Meta:
        model = Companies
        fields = (
            'company_id',
            'itn',
            'locality',
            'phones',
            'emails',
            'site',
            'name',
            'gps',
            'region',
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
