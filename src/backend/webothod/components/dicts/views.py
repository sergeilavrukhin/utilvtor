from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Regions, QueryType
from .serializers import RegionsSerializer, QueryTypesSerializer


class RegionsView(
    GenericViewSet,
):
    @staticmethod
    def list(request):
        regions = Regions.objects
        return Response(
            RegionsSerializer(
                regions,
                many=True
            ).data
        )


class QueryTypesView(
    GenericViewSet,
):
    @staticmethod
    def list(request):
        query_types = QueryType.objects
        return Response(
            QueryTypesSerializer(
                query_types,
                many=True,
            ).data
        )
