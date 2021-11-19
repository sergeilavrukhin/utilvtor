from django.urls import path
from .views import RegionsView, QueryTypesView

app_name = 'dicts'

urlpatterns = [
    path(
        'regions',
        RegionsView.as_view({'get': 'list'})
    ),
    path(
        'regions/map',
        RegionsView.as_view({'get': 'map'})
    ),
    path(
        'regions/activity/map',
        RegionsView.as_view({'get': 'activity_map'})
    ),
    path(
        'query_types',
        QueryTypesView.as_view({'get': 'list'})
    ),
]
