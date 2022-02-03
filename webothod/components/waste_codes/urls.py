from django.urls import path
from .views import WasteCodesView

app_name = 'waste_codes'

urlpatterns = [
    path(
        '',
        WasteCodesView.as_view({'get': 'list'})
    ),
    path(
        'map',
        WasteCodesView.as_view({'get': 'map'})
    ),
    path(
        'activity/map',
        WasteCodesView.as_view({'get': 'activity_map'})
    ),
    path(
        'code/<int:code>',
        WasteCodesView.as_view({'get': 'one'})
    ),
    path(
        'children/<int:code>',
        WasteCodesView.as_view({'get': 'children'})
    ),
]
