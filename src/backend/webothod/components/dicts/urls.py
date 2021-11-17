from django.urls import path
from .views import RegionsView, QueryTypesView

app_name = 'dicts'

urlpatterns = [
    path('regions', RegionsView.as_view({'get': 'list'}), name='dict_regions'),
    path('query_types', QueryTypesView.as_view({'get': 'list'}), name='dict_query_types'),
]
