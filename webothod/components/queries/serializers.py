from rest_framework import serializers

from .models import Queries
from ..dicts.serializers import RegionsSerializer, QueryTypesSerializer
from ..users.serializers import UserSerializer


class QueriesSerializer(serializers.ModelSerializer):
    region = RegionsSerializer(help_text='Регион')
    type = QueryTypesSerializer(help_text='Тип заявки')
    user = UserSerializer(help_text='Пользователь')
    created_at = serializers.SerializerMethodField(help_text='Дата и время создания')

    class Meta:
        model = Queries
        fields = ("pk", "type", "user", "region", "created_at", "waste", "description")

    @staticmethod
    def get_created_at(el):
        return el.created_at.timestamp()
