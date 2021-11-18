from django.urls import path

from .views import CompaniesView

app_name = 'companies'

urlpatterns = [
    path(
        '<str:itn>',
        CompaniesView.as_view({'get': 'one'}),
        name='companies_one',
    ),
    path(
        'by_code_limit/<int:code>',
        CompaniesView.as_view({'get': 'by_code_limit'}),
        name='companies_by_code_limit',
    ),
    path(
        'search/<int:code>',
        CompaniesView.as_view({'get': 'search'}),
        name='companies_search_by_code',
    ),
    path(
        'search/<int:code>/activity/<str:activity>',
        CompaniesView.as_view({'get': 'search'}),
        name='companies_search_by_code_by_activity',
    ),
    path(
        'search/region/<int:region>',
        CompaniesView.as_view({'get': 'search'}),
        name='companies_search_by_region',
    ),
    path(
        'search/region/<int:region>/page/<int:page>',
        CompaniesView.as_view({'get': 'search'}),
        name='companies_search_by_region_by_page',
    ),
    path(
        'codes_list/<str:itn>',
        CompaniesView.as_view({'get': 'codes_list'}),
        name='companies_codes_list',
    ),
]
