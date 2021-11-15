from django.urls import path
from . import views

app_name = 'companies'

urlpatterns = [
    path('', views.Companies.as_view(), name='companies_list'),
]
