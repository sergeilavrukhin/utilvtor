from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django.db.models import Q

from .models import Companies, CompanyWasteCodes
from .serializers import CompaniesSerializer, CompanyWasteCodesSerializer
from ..dicts.models import Regions
from ..dicts.serializers import RegionsSerializer


class CompaniesView(
    GenericViewSet,
):
    @staticmethod
    def list(request, page=1):
        companies = Companies.objects
        paginator = Paginator(companies.order_by('-actual_at', 'itn'), 10)
        return Response({
            "count": paginator.num_pages,
            "companies": CompaniesSerializer(
                paginator.page(page),
                many=True,
            ).data
        })

    @staticmethod
    def map(request):
        companies = Companies.objects.values('itn')
        return Response(
            companies
        )

    @staticmethod
    def one(request, itn):
        companies = Companies.objects.filter(
            itn=itn
        )
        return Response(
            CompaniesSerializer(
                companies.first()
            ).data
        )

    @staticmethod
    def by_code(request, code):
        companies_pk = CompanyWasteCodes.objects.filter(
            waste_code__code=code
        ).order_by('itn')[:3].values('company')

        companies = Companies.objects.filter(
            pk__in=companies_pk
        )
        return Response(
            CompaniesSerializer(
                companies,
                many=True,
            ).data
        )

    @staticmethod
    def search(request, search=None, region=None, activity=None, page=1):
        companies = Companies.objects
        companies_pk = CompanyWasteCodes.objects
        if search:
            companies_pk = companies_pk.filter(
                Q(waste_code__code=search.replace(' ', ''))
                |
                Q(company__name__icontains=search)
                |
                Q(company__itn__icontains=search)
                |
                Q(waste_code__name__icontains=search)
            )
            companies = companies.filter(
                pk__in=companies_pk.values('company')
            )
        if activity:
            companies_pk = companies_pk.filter(
                activity__contains=activity
            )
            companies = companies.filter(
                pk__in=companies_pk.values('company')
            )
        region_dict = {}
        if region:
            companies = companies.filter(
                region__code=region
            )
            region_dict = RegionsSerializer(Regions.objects.filter(code=region).first()).data

        paginator = Paginator(companies.order_by('-actual_at', 'itn'), 10)
        return Response({
            "region": region_dict,
            "count": paginator.num_pages,
            "companies": CompaniesSerializer(
                paginator.page(page),
                many=True,
            ).data
        })

    @staticmethod
    def codes_list(request, itn):
        company_waste_codes = CompanyWasteCodes.objects.filter(
            company__itn=itn
        )
        return Response(
            CompanyWasteCodesSerializer(
                company_waste_codes,
                many=True,
            ).data
        )
