from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Regions, QueryType
from .serializers import RegionsSerializer, QueryTypesSerializer


class RegionsView(
    GenericViewSet,
):

    def get_queryset(self):
        return Regions.objects

    def list(self, request):
        result = self.get_queryset().filter()
        return Response(RegionsSerializer(result, many=True).data)


class QueryTypesView(
    GenericViewSet,
):

    def get_queryset(self):
        return QueryType.objects

    def list(self, request):
        result = self.get_queryset().filter()
        return Response(QueryTypesSerializer(result, many=True).data)
