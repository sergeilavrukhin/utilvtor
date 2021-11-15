from django.urls import path
from . import views

app_name = 'queries'

urlpatterns = [
    path('', views.Queries.as_view(), name='queries_list'),
]
