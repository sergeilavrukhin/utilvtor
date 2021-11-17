from django.urls import path

from .views import CompaniesView

app_name = 'companies'

urlpatterns = [
    path(
        '',
        CompaniesView.as_view({'get': 'list'}),
        name='companies',
    ),
    path(
        '<int:itn>',
        CompaniesView.as_view({'get': 'one'}),
        name='companies_one',
    ),
    path(
        'by_code/<int:code>',
        CompaniesView.as_view({'get': 'by_code'}),
        name='companies_by_code',
    ),
    path(
        'by_region/<int:region>',
        CompaniesView.as_view({'get': 'by_region'}),
        name='companies_by_region',
    ),
    path(
        'by_region/<int:region>/page/<int:page>',
        CompaniesView.as_view({'get': 'by_region'}),
        name='companies_by_region_page',
    ),
]
