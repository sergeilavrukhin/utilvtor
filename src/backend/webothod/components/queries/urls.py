from django.urls import path
from .views import QueriesView

app_name = 'queries'

urlpatterns = [
    path(
        '',
        QueriesView.as_view({'get': 'list', 'post': 'create'})
    ),
    path(
        'map',
        QueriesView.as_view({'get': 'map'})
    ),
    path(
        '<int:pk>',
        QueriesView.as_view({'get': 'one'})
    ),
    path(
        'page/<int:page>',
        QueriesView.as_view({'get': 'list'})
    ),
]
