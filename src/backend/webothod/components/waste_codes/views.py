from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import WasteCodes
from .serializers import WasteCodesSerializer
from ..dicts.models import activities


class WasteCodesView(
    GenericViewSet,
):
    @staticmethod
    def list(request):
        waste_codes = WasteCodes.objects.filter(parent_code='')
        return Response(
            WasteCodesSerializer(
                waste_codes,
                many=True,
            ).data
        )

    @staticmethod
    def map(request):
        codes = WasteCodes.objects.values('code')
        return Response(
            codes
        )

    @staticmethod
    def activity_map(request):
        codes = WasteCodes.objects.values('code')
        code_activity = []
        for code in codes:
            for activity in activities:
                data = {"code": code["code"], "activity": activity}
                code_activity.append(data)
        return Response(
            code_activity
        )

    @staticmethod
    def one(request, code=''):
        waste_codes = WasteCodes.objects.filter(code=code)
        return Response(
            WasteCodesSerializer(
                waste_codes.first()
            ).data
        )

    @staticmethod
    def children(request, code=''):
        waste_codes = WasteCodes.objects.filter(parent_code=code)
        return Response(
            WasteCodesSerializer(
                waste_codes,
                many=True
            ).data
        )
