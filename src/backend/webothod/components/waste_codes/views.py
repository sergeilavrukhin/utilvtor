from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import WasteCodes
from .serializers import WasteCodesSerializer


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
