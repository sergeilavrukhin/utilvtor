from django.urls import path
from .views import WasteCodesView

app_name = 'waste_codes'

urlpatterns = [
    path(
        '',
        WasteCodesView.as_view({'get': 'list'}),
        name='waste_codes',
    ),
    path(
        'code/<int:code>',
        WasteCodesView.as_view({'get': 'one'}),
        name='waste_codes',
    ),
    path(
        'children/<int:code>',
        WasteCodesView.as_view({'get': 'children'}),
        name='waste_codes',
    ),
]
