from collections import OrderedDict

from django.core.paginator import InvalidPage
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import PageNumberPagination

from .models import Companies, CompanyWasteCodes
from .serializers import CompaniesSerializer, CompanyWasteCodesSerializer
from ..waste_codes.models import WasteCodes
from ..waste_codes.serializers import WasteCodesSerializer


class CompaniesPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page = 1

    def set_page_number(self, page):
        self.page = page

    def get_page_number(self, request, paginator):
        page_number = self.page
        if page_number in self.last_page_strings:
            page_number = paginator.num_pages
        return page_number

    def paginate_queryset(self, queryset, request, view=None):
        page_size = self.get_page_size(request)
        if not page_size:
            return None

        paginator = self.django_paginator_class(queryset, page_size)
        page_number = self.page
        if page_number in self.last_page_strings:
            page_number = paginator.num_pages

        try:
            self.page = paginator.page(page_number)
        except InvalidPage as exc:
            msg = self.invalid_page_message.format(
                page_number=page_number, message=str(exc)
            )
            raise NotFound(msg)

        if paginator.num_pages > 1 and self.template is not None:
            self.display_page_controls = True

        self.request = request
        return list(self.page)

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.num_pages),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))


class CompaniesView(
    GenericViewSet,
):
    pagination_class = CompaniesPagination
    serializer_class = CompaniesSerializer

    def paginate_page_queryset(self, queryset, request, page):
        self.paginator.set_page_number(page)
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, request, view=self)

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
        )[:3].values('company')

        companies = Companies.objects.filter(
            pk__in=companies_pk
        )
        return Response(
            CompaniesSerializer(
                companies,
                many=True,
            ).data
        )

    def paginate(self, companies, request, page):
        paginate_page_queryset = self.paginate_page_queryset(
            companies,
            request,
            page,
        ),
        return self.get_paginated_response(
            paginate_page_queryset
        )

    def search(self, request, region=None, code=None, activity=None, page=1):
        companies = Companies.objects
        companies_pk = CompanyWasteCodes.objects
        if code:
            companies_pk = companies_pk.filter(
                waste_code__code=code
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
        if region:
            companies = companies.filter(
                region__code=region
            )
        print(companies)
        return self.paginate(companies.order_by('itn'), request, page)

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
