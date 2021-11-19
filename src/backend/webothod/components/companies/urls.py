from django.urls import path

from .views import CompaniesView

app_name = 'companies'

urlpatterns = [
    path(
        '',
        CompaniesView.as_view({'get': 'list'})
    ),
    path(
        'map',
        CompaniesView.as_view({'get': 'map'})
    ),
    path(
        'page/<int:page>',
        CompaniesView.as_view({'get': 'list'})
    ),
    path(
        'by_code/<int:code>',
        CompaniesView.as_view({'get': 'by_code'})
    ),
    path(
        'search/<str:search>',
        CompaniesView.as_view({'get': 'search'})
    ),
    path(
        'search/region/<int:region>',
        CompaniesView.as_view({'get': 'search'})
    ),
    path(
        'search/region/<int:region>/page/<int:page>',
        CompaniesView.as_view({'get': 'search'})
    ),
    path(
        'search/region/<int:region>/activity/<str:activity>',
        CompaniesView.as_view({'get': 'search'})
    ),
    path(
        'search/region/<int:region>/activity/<str:activity>/page/<int:page>',
        CompaniesView.as_view({'get': 'search'})
    ),
    path(
        'search/<str:search>/activity/<str:activity>',
        CompaniesView.as_view({'get': 'search'})
    ),
    path(
        'search/<str:search>/activity/<str:activity>/page/<int:page>',
        CompaniesView.as_view({'get': 'search'})
    ),
    path(
        'search/<str:search>/region/<int:region>',
        CompaniesView.as_view({'get': 'search'})
    ),
    path(
        'search/<str:search>/region/<int:region>/page/<int:page>',
        CompaniesView.as_view({'get': 'search'})
    ),
    path(
        'search/<str:search>/region/<int:region>/activity/<str:activity>',
        CompaniesView.as_view({'get': 'search'})
    ),
    path(
        'search/<str:search>/region/<int:region>/activity/<str:activity>/page/<int:page>',
        CompaniesView.as_view({'get': 'search'})
    ),
    path(
        'codes_list/<str:itn>',
        CompaniesView.as_view({'get': 'codes_list'})
    ),
    path(
        '<str:itn>',
        CompaniesView.as_view({'get': 'one'})
    ),
]
