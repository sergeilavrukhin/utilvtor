from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import WasteCodes
from .serializers import WasteCodesSerializer


class WasteCodesView(
    GenericViewSet,
):

    def get_queryset(self):
        return WasteCodes.objects

    def list(self, request):
        result = self.get_queryset().filter(parent_code='')
        return Response(WasteCodesSerializer(result, many=True).data)

    def one(self, request, code=''):
        result = self.get_queryset().filter(code=code).first()
        return Response(WasteCodesSerializer(result).data)

    def children(self, request, code=''):
        result = self.get_queryset().filter(parent_code=code)
        return Response(WasteCodesSerializer(result, many=True).data)
