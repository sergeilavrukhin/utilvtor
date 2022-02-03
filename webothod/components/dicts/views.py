from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Regions, QueryType, activities
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

    @staticmethod
    def map(request):
        regions = Regions.objects.values('code')
        return Response(
            regions
        )

    @staticmethod
    def activity_map(request):
        regions = Regions.objects.values('code')
        region_activity = []
        for region in regions:
            for activity in activities:
                data = {"code": region["code"], "activity": activity}
                region_activity.append(data)
        return Response(
            region_activity
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
