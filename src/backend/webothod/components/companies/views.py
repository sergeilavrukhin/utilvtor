from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import PageNumberPagination

from .models import Companies, CompanyWasteCodes
from .serializers import CompaniesSerializer


class CompaniesPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'


class CompaniesView(
    GenericViewSet,
):
    pagination_class = CompaniesPagination
    serializer_class = CompaniesSerializer

    def get_queryset(self):
        return Companies.objects

    def list(self, request):
        result = self.get_queryset().filter()
        return Response(CompaniesSerializer(result, many=True).data)

    def one(self, request, itn):
        result = self.get_queryset().filter(itn=itn).first()
        return Response(CompaniesSerializer(result).data)

    def by_code(self, request, code):
        waste_codes = CompanyWasteCodes.objects.filter(waste_code__code=code)[:3].values('pk')
        result = self.get_queryset().filter(pk__in=waste_codes)
        return Response(CompaniesSerializer(result, many=True).data)

    def by_region(self, request, region, page=1):
        result = self.get_queryset().filter(region__code=region).order_by('pk')
        page = self.paginate_queryset(result)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)
